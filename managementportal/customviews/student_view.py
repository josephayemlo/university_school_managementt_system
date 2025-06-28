from django.shortcuts import render, redirect,  get_object_or_404
from core.forms import StudentForm
from django.contrib import messages
from django.urls import reverse
from core.models import Student
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.

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
                print('User  Created ')

                # Manually create Student object
                student = Student.objects.create(
                    admin=user,
                    matric_no=matric_no,
                    course_of_study=course_of_study,
                    level=level
                )
                print('Student  Created ')


                messages.success(request, "Student successfully added.")
                return redirect('management_home')

            except Exception as e:
                messages.error(request, "Could not add student: " + str(e))
        else:
            messages.error(request, "Please fill all required fields correctly.")

    return render(request, 'management/partials/student/add_student_template.html', context)


def student_list(request):
    students = User.objects.filter(user_type=4)
    return render(request, 'management/partials/student/student_list.html', {'students': students})


def edit_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    form = StudentForm(request.POST or None, instance=student)
    context = {
        'form': form,
        'student_id': student_id,
        'page_title': 'Edit Student'
    }
    if request.method == 'POST':
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            address = form.cleaned_data.get('address')
            email = form.cleaned_data.get('email')
            gender = form.cleaned_data.get('gender')
            password = form.cleaned_data.get('password') or None
             # Student fields
            matric_no = form.cleaned_data.get('matric_no')
            course_of_study = form.cleaned_data.get('course_of_study')
            level = form.cleaned_data.get('level')


            try:
                user = User.objects.get(id=student.admin.id)                
                user.email = email
                if password != None:
                    user.set_password(password)
                user.first_name = first_name
                user.last_name = last_name
                user.gender = gender
                user.address = address
                user.save()
                student.matric_no = matric_no
                student.course_of_study = course_of_study
                student.level = level

                student.save()
                messages.success(request, "Successfully Updated")
                return redirect(reverse('edit_student', args=[student_id]))
            except Exception as e:
                messages.error(request, "Could Not Update " + str(e))
        else:
            messages.error(request, "Please Fill Form Properly!")
    else:
        return render(request, "management/partials/student/edit_student_template.html", context)


def delete_student(request, student_id):
    student = get_object_or_404(User, student__id=student_id)
    student.delete()
    messages.success(request, "Student deleted successfully!")
    return redirect(reverse('student_list'))

