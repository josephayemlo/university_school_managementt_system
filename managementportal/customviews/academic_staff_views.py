from django.shortcuts import render, redirect,  get_object_or_404
from core.forms import AcademicStaffForm
from django.contrib import messages
from core.models import AcademicStaff, AssignCourse
from django.urls import reverse
from django.contrib.auth import get_user_model
User = get_user_model()
from core.forms import AssignCourseForm
from django.http import JsonResponse
from django.db import IntegrityError











# assign course
def assign_course(request):
    form = AssignCourseForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "✅ Course assigned to academic staff successfully.")
            except IntegrityError as e:
                print("❌ IntegrityError:", e)
                messages.error(request, "⚠️ This course is already assigned to this staff.")
        else:
            print("❌ Form is invalid:", form.errors)
            messages.error(request, "❌ Invalid form submission.")

        # Always redirect after POST (Post/Redirect/Get pattern)
        return redirect(request.path)

    return render(request, 'management/partials/academicstaff/assign_course.html', {'form': form})


# manage/view
def manage_assigned_course(request):
    assigned_course = AssignCourse.objects.all()
    context= {"assigned_course":assigned_course}
    return render(request, 'management/partials/academicstaff/manage_assigned_course.html', context)

# edit
def edit_assigned_course(request, assigned_course_id):
    assigned_course = get_object_or_404(AssignCourse, id=assigned_course_id)
    if request.method == 'POST':
        form = AssignCourseForm(request.POST, instance=assigned_course)
        if form.is_valid():
            form.save()
            messages.success(request, 'assigned course Updated Sucessfully')
            return redirect(request.path)
    else:
        form = AssignCourseForm(instance=assigned_course)
    context = {
        "form": form,
        "assigned_course": assigned_course
    }

    return render(request, 'management/partials/academicstaff/edit_assigned_course.html', context)

# delete
def delete_assigned_course(request, assigned_course_id):
    if request.method == 'POST':
        assigned_course = get_object_or_404(AssignCourse, id=assigned_course_id)
        assigned_course.delete()
        print("assigned_course deleted")
        messages.success(request, 'assigned_course Deleted Sucessfully')
        return render(request,'management/partials/success.html')
    return render(request, 'management/partials/academicstaff/manage_assigned_course.html')
    



# add academic staff
def add_academicstaff(request):
    
    form = AcademicStaffForm(request.POST or None, request.FILES or None)
    context = {'form': form, 'page_title': 'Add Academic Staff'}
    if request.method == 'POST':
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            address = form.cleaned_data.get('address')
            email = form.cleaned_data.get('email')
            gender = form.cleaned_data.get('gender')
            password = form.cleaned_data.get('password')
        
            try:
                user = User.objects.create_user(
                    email=email, password=password, user_type=2, first_name=first_name, last_name=last_name)
                user.gender = gender
                user.address = address
                user.save()
                messages.success(request, "Academic Staff Successfully Added")
                return redirect(request.path)


            except Exception as e:
                messages.error(request, "Could Not Add " + str(e))
        else:
            messages.error(request, "Please fulfil all requirements")

    return render(request, 'management/partials/academicstaff/add_academicstaff_template.html', context)


# list
def academicstaff_list(request):
    academicstaffs = User.objects.filter(user_type=2)
    return render(request, 'management/partials/academicstaff/academicstaff_list.html', {'academicstaffs': academicstaffs})
# edit
def edit_academicstaff(request, academicstaff_id):
    academicstaff = get_object_or_404(AcademicStaff, id=academicstaff_id)
    form = AcademicStaffForm(request.POST or None, instance=academicstaff)
    context = {
        'form': form,
        'academicstaff_id': academicstaff_id,
        'page_title': 'Edit Academic Staff'
    }
    if request.method == 'POST':
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            address = form.cleaned_data.get('address')
            email = form.cleaned_data.get('email')
            gender = form.cleaned_data.get('gender')
            password = form.cleaned_data.get('password') or None
            try:
                user = User.objects.get(id=academicstaff.admin.id)                
                user.email = email
                if password != None:
                    user.set_password(password)
                user.first_name = first_name
                user.last_name = last_name
                user.gender = gender
                user.address = address
                user.save()
                academicstaff.save()
                messages.success(request, "Successfully Updated")
                return redirect(reverse('edit_academicstaff', args=[academicstaff_id]))
            except Exception as e:
                messages.error(request, "Could Not Update " + str(e))
        else:
            messages.error(request, "Please Fill Form Properly!")
    else:
        return render(request, "management/partials/academicstaff/edit_academicstaff_template.html", context)

# delete
def delete_academicstaff(request, academicstaff_id):
    academicstaff = get_object_or_404(User, academicstaff__id=academicstaff_id)
    academicstaff.delete()
    messages.success(request, "academicstaff deleted successfully!")
    return redirect(reverse('academicstaff_list'))


