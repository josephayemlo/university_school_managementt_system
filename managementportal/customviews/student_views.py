from django.shortcuts import render, redirect,  get_object_or_404
from core.forms import StudentForm
from django.contrib import messages
from django.urls import reverse
from core.models import Student
from django.contrib.auth import get_user_model
User = get_user_model()

from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

# permission check
def is_custom_superuser(user):
    return user.is_authenticated and user.user_type == '1'

# add
@login_required
@user_passes_test(is_custom_superuser)
def add_student(request):
    form = StudentForm(request.POST or None, request.FILES or None)
    context = {'form': form, 'page_title': 'Add Student'}

    if request.method == 'POST':
        if form.is_valid():
            # User fields
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            address = form.cleaned_data.get('address')
            email = form.cleaned_data.get('email')
            gender = form.cleaned_data.get('gender')
            password = form.cleaned_data.get('password')

            # Student fields
            matric_no = form.cleaned_data.get('matric_no')
            course_of_study = form.cleaned_data.get('course_of_study')
            level = form.cleaned_data.get('level')

            try:
                # Create user with all fields at once
                user = User.objects.create_user(
                    email=email,
                    password=password,
                    user_type=4,
                    first_name=first_name,
                    last_name=last_name,
                    gender=gender,
                    address=address
                )
                # Manually create Student object
                student = Student.objects.create(
                    admin=user,
                    matric_no=matric_no,
                    course_of_study=course_of_study,
                    level=level
                )
                messages.success(request, "Student successfully added.")
                return render(request,'management/partials/success.html')
            except Exception as e:
                messages.error(request, "Could not add student: " + str(e))
        else:
            messages.error(request, "Please fill all required fields correctly.")
    return render(request, 'management/partials/student/add_student.html', context)


@login_required
@user_passes_test(is_custom_superuser)
def manage_student(request):
    students = Student.objects.select_related('admin').order_by('course_of_study__name')
    return render(request, 'management/partials/student/manage_student.html', {'students': students})


@login_required
@user_passes_test(is_custom_superuser)
def edit_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    user = student.admin  # linked User object
    form = StudentForm(request.POST or None, instance=student)

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
                student.matric_no = form.cleaned_data['matric_no']
                student.course_of_study = form.cleaned_data['course_of_study']
                student.level = form.cleaned_data['level']
                student.save()

                messages.success(request, "Successfully updated student.")
                return redirect(request.path)
            
            except Exception as e:
                messages.error(request, f"Could not update student: {e}")
        else:
            messages.error(request, "Please fill out the form correctly.")

    context = {
        'form': form,
        'student': student,
        'page_title': 'Edit Student'
    }
    return render(request, "management/partials/student/edit_student.html", context)

# delete
@login_required
@user_passes_test(is_custom_superuser)
def delete_student(request, student_id):
    if request.method == 'POST':
        student = get_object_or_404(Student, id=student_id)
        student.delete()
        print("student deleted")
        messages.success(request, 'student Deleted Sucessfully')
        return render(request,'management/partials/success.html')
    return render(request, 'management/partials/student/manage_student.html')
    