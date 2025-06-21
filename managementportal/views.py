from django.shortcuts import render, redirect,  get_object_or_404
from accounts.forms import AcademicStaffForm, NonAcademicStaffForm, StudentForm, CustomUser, AspirantStudentForm
from django.contrib import messages
from accounts.models import CustomUser, AcademicStaff, NonAcademicStaff
from django.urls import reverse
from studentportal.models import Student
# Create your views here.



def management_home (request):
    total_academicstaff = AcademicStaff.objects.all().count()
    total_nonacademicstaff = NonAcademicStaff.objects.all().count()
    total_students = Student.objects.all().count()



    male_count = Student.objects.filter(admin__gender='M').count()
    female_count = Student.objects.filter(admin__gender='F').count()
    total = male_count + female_count or 1  # avoid division by zero

    male_percent = round((male_count / total) * 100)
    female_percent = round((female_count / total) * 100)

    
    context = {
        'total_academicstaff': total_academicstaff,
        'total_nonacademicstaff': total_nonacademicstaff,
        'total_students': total_students,
        'male_percent': male_percent,
        'female_percent': female_percent,
        'male_count': male_count,
        'female_count': female_count       
    }
    return render(request, 'management_home.html', context)



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
                user = CustomUser.objects.create_user(
                    email=email, password=password, user_type=2, first_name=first_name, last_name=last_name)
                user.gender = gender
                user.address = address
                user.save()
                messages.success(request, "Academic Staff Successfully Added")
                return redirect('management_home')

            except Exception as e:
                messages.error(request, "Could Not Add " + str(e))
        else:
            messages.error(request, "Please fulfil all requirements")

    return render(request, 'add_academicstaff_template.html', context)



def add_nonacademicstaff(request):
    form = NonAcademicStaffForm(request.POST or None, request.FILES or None)
    context = {'form': form, 'page_title': 'Add NonAcademic Staff'}
    if request.method == 'POST':
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            address = form.cleaned_data.get('address')
            email = form.cleaned_data.get('email')
            gender = form.cleaned_data.get('gender')
            password = form.cleaned_data.get('password')
        
            try:
                user = CustomUser.objects.create_user(
                    email=email, password=password, user_type=3, first_name=first_name, last_name=last_name)
                user.gender = gender
                user.address = address
                user.save()
                messages.success(request, "NonAcademic Staff Successfully Added")
                return redirect('management_home')

            except Exception as e:
                messages.error(request, "Could Not Add " + str(e))
        else:
            messages.error(request, "Please fulfil all requirements")

    return render(request, 'add_nonacademicstaff_template.html', context)


def add_student(request):
    form = StudentForm(request.POST or None, request.FILES or None)
    context = {'form': form, 'page_title': 'Add Student'}

    if request.method == 'POST':
        if form.is_valid():
            # CustomUser fields
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
                user = CustomUser.objects.create_user(
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

    return render(request, 'add_student_template.html', context)


def add_aspirant_student(request):
    form = AspirantStudentForm(request.POST or None, request.FILES or None)
    context = {'form': form, 'page_title': 'Add Aspirant Student'}
    if request.method == 'POST':
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            address = form.cleaned_data.get('address')
            email = form.cleaned_data.get('email')
            gender = form.cleaned_data.get('gender')
            password = form.cleaned_data.get('password')
        
            try:
                user = CustomUser.objects.create_user(
                    email=email, password=password, user_type=5, first_name=first_name, last_name=last_name)
                user.gender = gender
                user.address = address
                user.save()
                messages.success(request, "Aspirant Student Successfully Added")
                return redirect('management_home')

            except Exception as e:
                messages.error(request, "Could Not Add " + str(e))
        else:
            messages.error(request, "Please fulfil all requirements")

    return render(request, 'add_aspirant_student_template.html', context)



def academicstaff_list(request):
    academicstaffs = CustomUser.objects.filter(user_type=2)
    return render(request, 'staff/academicstaff_list.html', {'academicstaffs': academicstaffs})

def nonacademicstaff_list(request):
    nonacademicstaffs = CustomUser.objects.filter(user_type=3)
    return render(request, 'staff/nonacademicstaff_list.html', {'nonacademicstaffs': nonacademicstaffs})

def student_list(request):
    students = CustomUser.objects.filter(user_type=4)
    return render(request, 'student/student_list.html', {'students': students})

def aspirant_student_list(request):
    aspirantstudents = CustomUser.objects.filter(user_type=5)
    return render(request, 'student/aspirant_student_list.html', {'aspirantstudents': aspirantstudents})


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
                user = CustomUser.objects.get(id=academicstaff.admin.id)                
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
        return render(request, "management/edit_academicstaff_template.html", context)



def edit_nonacademicstaff(request, nonacademicstaff_id):
    nonacademicstaff = get_object_or_404(NonAcademicStaff, id=nonacademicstaff_id)
    form = NonAcademicStaffForm(request.POST or None, instance=nonacademicstaff)
    context = {
        'form': form,
        'nonacademicstaff_id': nonacademicstaff_id,
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
                user = CustomUser.objects.get(id=nonacademicstaff.admin.id)                
                user.email = email
                if password != None:
                    user.set_password(password)
                user.first_name = first_name
                user.last_name = last_name
                user.gender = gender
                user.address = address
                user.save()
                nonacademicstaff.save()
                messages.success(request, "Successfully Updated")
                return redirect(reverse('edit_nonacademicstaff', args=[nonacademicstaff_id]))
            except Exception as e:
                messages.error(request, "Could Not Update " + str(e))
        else:
            messages.error(request, "Please Fill Form Properly!")
    else:
        return render(request, "management/edit_nonacademicstaff_template.html", context)

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
                user = CustomUser.objects.get(id=student.admin.id)                
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
        return render(request, "management/edit_student_template.html", context)


def delete_academicstaff(request, academicstaff_id):
    academicstaff = get_object_or_404(CustomUser, academicstaff__id=academicstaff_id)
    academicstaff.delete()
    messages.success(request, "academicstaff deleted successfully!")
    return redirect(reverse('academicstaff_list'))


def delete_nonacademicstaff(request, nonacademicstaff_id):
    nonacademicstaff = get_object_or_404(CustomUser, nonacademicstaff__id=nonacademicstaff_id)
    nonacademicstaff.delete()
    messages.success(request, "nonacademicstaff deleted successfully!")
    return redirect(reverse('nonacademicstaff_list'))

def delete_student(request, student_id):
    student = get_object_or_404(CustomUser, student__id=student_id)
    student.delete()
    messages.success(request, "Student deleted successfully!")
    return redirect(reverse('student_list'))

