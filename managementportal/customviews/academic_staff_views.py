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
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test


# permission check
def is_custom_superuser(user):
    return user.is_authenticated and user.user_type == '1'


# assign course
@login_required
@user_passes_test(is_custom_superuser)
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
@login_required
@user_passes_test(is_custom_superuser)
def manage_assigned_course(request):
    assigned_course = AssignCourse.objects.all()
    context= {"assigned_course":assigned_course}
    return render(request, 'management/partials/academicstaff/manage_assigned_course.html', context)

# edit
@login_required
@user_passes_test(is_custom_superuser)
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
@login_required
@user_passes_test(is_custom_superuser)
def delete_assigned_course(request, assigned_course_id):
    if request.method == 'POST':
        assigned_course = get_object_or_404(AssignCourse, id=assigned_course_id)
        assigned_course.delete()
        print("assigned_course deleted")
        messages.success(request, 'assigned_course Deleted Sucessfully')
        return render(request,'management/partials/success.html')
    return render(request, 'management/partials/academicstaff/manage_assigned_course.html')
    


# add academic staff
@login_required
@user_passes_test(is_custom_superuser)
def add_academicstaff(request):
    form = AcademicStaffForm(request.POST or None, request.FILES or None)
    context = {'form': form, 'page_title': 'Add AcademicStaff'}

    if request.method == 'POST':
        if form.is_valid():
            # User fields
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            address = form.cleaned_data.get('address')
            email = form.cleaned_data.get('email')
            gender = form.cleaned_data.get('gender')
            password = form.cleaned_data.get('password')

            # Extra fields
            position = form.cleaned_data.get('position')
            role = form.cleaned_data.get('role')
            department = form.cleaned_data.get('department')


            try:
                # Create user with all fields at once
                user = User.objects.create_user(
                    email=email,
                    password=password,
                    user_type=2,
                    first_name=first_name,
                    last_name=last_name,
                    gender=gender,
                    address=address
                )
                # Manually create Academicstaff object
                academicstaff = AcademicStaff.objects.create(
                    admin=user,
                    position=position,
                    role=role,
                    department=department
                )
                messages.success(request, "Staff successfully added.")
                return redirect(request.path)
            except Exception as e:
                messages.error(request, "Could not add Staff: " + str(e))
        else:
            messages.error(request, "Please fill all required fields correctly.")
    return render(request, 'management/partials/academicstaff/add_academicstaff.html', context)



# list
@login_required
@user_passes_test(is_custom_superuser)
def manage_academicstaff(request):
    academicstaff = AcademicStaff.objects.select_related('admin').order_by('admin__last_name')
    return render(request, 'management/partials/academicstaff/manage_academicstaff.html', {'academicstaff': academicstaff})

# edit
@login_required
@user_passes_test(is_custom_superuser)
def edit_academicstaff(request, academicstaff_id):
    academicstaff = get_object_or_404(AcademicStaff, id=academicstaff_id)
    user = academicstaff.admin  # linked User object
    form = AcademicStaffForm(request.POST or None, instance=academicstaff)

    if request.method == 'POST':
        if form.is_valid():
            try:
                # Update User fields
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.email = form.cleaned_data['email']
                user.address = form.cleaned_data['address']
                user.gender = form.cleaned_data['gender']
                
                password = form.cleaned_data.get('password')
                if password:
                    user.set_password(password)
                user.save()

                # Update Student fields
                academicstaff.position = form.cleaned_data['position']
                academicstaff.role = form.cleaned_data['role']
                academicstaff.department = form.cleaned_data['department']

                academicstaff.save()

                messages.success(request, "Successfully updated Staff.")
                return redirect(request.path)
            
            except Exception as e:
                messages.error(request, f"Could not update student: {e}")
        else:
            messages.error(request, "Please fill out the form correctly.")

    context = {
        'form': form,
        'academicstaff': academicstaff,
    }
    return render(request, "management/partials/academicstaff/edit_academicstaff.html", context)

# delete
@login_required
@user_passes_test(is_custom_superuser)
def delete_academicstaff(request, academicstaff_id):
    if request.method == 'POST':
        academicstaff = get_object_or_404(AcademicStaff, id=academicstaff_id)
        academicstaff.delete()
        print("academicstaff deleted")
        messages.success(request, 'academicstaff Deleted Sucessfully')
        return render(request,'management/partials/success.html')
    return render(request, 'management/partials/academicstaff/manage_academicstaff.html')
    