from django.shortcuts import render, redirect, get_object_or_404
from .forms import UndergraduateApplicationForm, ScholarshipApplicationForm
from accounts.forms import CustomUser
from accounts.models import CustomUser

from django.core.mail import EmailMessage
from .models import PersonalStatement
import mimetypes
import os
from django.http.response import HttpResponse
from django.conf import settings
# Create your views here.
from .forms import *
from django.contrib import messages
from studentportal.models import AspirantStudent
import random
from django.db import transaction
from .models import *
from django.http import JsonResponse




def add_faculty(request):
    form = FacultyForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "Faculty added successfully.")
        return redirect('management_home')
    return render(request, 'core/add_faculty.html', {'form': form})





def add_academic_calender(request):
    form = AcademicCalenderForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "Academic Calender added successfully.")
        return render(request, 'management/partials/success.html')
    return render(request, 'management/partials/add_academic_calender.html', {'form': form})

def manage_academic_calender(request):
    academic_calender = AcademicCalendar.objects.all()
    context= {"academic_calender":academic_calender}

    return render(request, 'management/partials/manage_academic_calender.html', context)

def edit_academic_calender(request, academic_calender_id):
    academic_calender = get_object_or_404(AcademicCalendar, id=academic_calender_id)
    print("single academic calender loaded")

    if request.method == 'POST':
        print("request is post")

        form = AcademicCalenderForm(request.POST, instance=academic_calender)
        if form.is_valid():
            form.save()
            messages.success(request, 'Academic Calender Updated Sucessfully')
            return render(request,'management/partials/success.html')
    else:
        form = AcademicCalenderForm(instance=academic_calender)

    context = {
        "form": form,
        "academic_calender": academic_calender
    }

    return render(request, 'management/partials/edit_academic_calender.html', context)



def edit_level_course(request, course_id):
    levelcourse = get_object_or_404(LevelCourse, id=course_id)

    if request.method == 'POST':
        form = LevelCourseForm(request.POST, instance=levelcourse)
        if form.is_valid():
            form.save()
            messages.success(request, 'Level Course Updated Sucessfully')
            return render(request,'management/partials/success.html')
    else:
        form = LevelCourseForm(instance=levelcourse)

    context = {
        "form": form,
        "levelcourse": levelcourse
    }

    return render(request, 'management/partials/edit_level_course.html', context)


def delete_level_course(request, course_id):
    if request.method == 'POST':
        levelcourse = get_object_or_404(LevelCourse, id=course_id)
        levelcourse.delete()
        messages.success(request, 'Level Course Deleted Sucessfully')
        return render(request,'management/partials/success.html')
    return render(request, 'management/partials/manage_level_course.html')
    
def manage_level_course(request):
    levelcourse = LevelCourse.objects.all()
    context= {"levelcourse":levelcourse}

    return render(request, 'management/partials/manage_level_course.html', context)


def assign_level_course(request):
    if request.method == 'POST':
        form = LevelCourseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Course Assigned to Level Sucessfully')
            return render(request,'management/partials/success.html')
    else:
        form = LevelCourseForm()
    return render(request, 'management/partials/assign_course_to_level.html', {'form':form})




def delete_course(request, course_id):
    if request.method == 'POST':
        course = get_object_or_404(Course, id=course_id)
        course.delete()
        print("course deleted")
        messages.success(request, 'Course Deleted Sucessfully')
        return render(request,'management/partials/success.html')
    return render(request, 'management/partials/manage_course.html')
    



def edit_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, 'Course Updated Sucessfully')
            return render(request,'management/partials/success.html')
    else:
        form = CourseForm(instance=course)

    context = {
        "form": form,
        "course": course
    }

    return render(request, 'management/partials/edit_course.html', context)


def manage_course_of_study(request):
    course_of_study = CourseOfStudy.objects.all()
    context= {"course_of_study":course_of_study}

    return render(request, 'management/partials/manage_course_of_study.html', context)




def delete_course_of_study(request, course_id):
    if request.method == 'POST':
        course_of_study = get_object_or_404(CourseOfStudy, id=course_id)
        course_of_study.delete()
        messages.success(request, 'Course of Study Deleted Sucessfully')
        return render(request,'management/partials/success.html')
    return render(request, 'management/partials/manage_course_of_study.html')
    



def edit_course_of_study(request, course_id):
    course_of_study = get_object_or_404(CourseOfStudy, id=course_id)

    if request.method == 'POST':
        form = CourseOfStudyForm(request.POST, instance=course_of_study)
        if form.is_valid():
            form.save()
            messages.success(request, 'Course of Study Updated Sucessfully')
            return render(request,'management/partials/success.html')
    else:
        form = CourseOfStudyForm(instance=course_of_study)

    context = {
        "form": form,
        "course_of_study": course_of_study
    }

    return render(request, 'management/partials/edit_course_of_study.html', context)


def manage_course(request):
    course = Course.objects.all()
    context= {"course":course}

    return render(request, 'management/partials/manage_course.html', context)

def result_and_assessment(request):
    return render (request, 'management/partials/result_and_assessment_links.html')


def department_and_faculty(request):
    return render (request, 'management/partials/department_and_faculty_links.html')

def session_and_calender(request):
    return render (request, 'management/partials/session_and_calender_links.html')



def course_and_academic(request):
    return render (request, 'management/partials/course_and_academic_links.html')

def student_management(request):
    return render (request, 'management/partials/student_links.html')

def add_course(request):
    form = CourseForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Course added sucessfully')
        return render(request, 'management/partials/success.html')
    return render(request, 'management/partials/add_course.html', {'form': form})




def add_department(request):
    form = DepartmentForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "Department added successfully.")
        return redirect('management_home')
    return render(request, 'core/add_department.html', {'form': form})

def add_course_of_study(request):
    form = CourseOfStudyForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "Course of Study added successfully.")
        return render(request, 'management/partials/success.html')
    return render(request, 'management/partials/add_course_of_study.html', {'form': form})

def personal_statement_download(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = 'Writing-a-Personal-Statement.pdf'
    filepath = BASE_DIR + '/media/personal_statement/' + filename
    path = open(filepath, 'rb')
    mime_type, _ = mimetypes.guess_type(filepath)
    response = HttpResponse(path, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response


def home (request):
    return render(request, 'home.html')


def apply (request):
    return render(request, 'core/apply.html')

def apply_Undergraduate_Process (request):
    
    file_name = 'personal_statement/Writing-a-Personal-Statement.pdf'
    file_stats = os.stat(os.path.join(settings.MEDIA_ROOT, file_name))
    file_size = file_stats.st_size
    context={
        'file_size': file_size,
        'file_name': file_name
    }

  
    return render(request, 'core/apply_undergraduate_process.html', context)



def apply_Undergraduate (request):
    return render(request, 'core/apply_undergraduate.html')


def apply_Postgraduate (request):
    return render(request, 'core/apply_postgraduate.html')

# scholarship form view
def scholarship_Application_Form_View(request):
    if request.method == 'POST':
        form = ScholarshipApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['first_name']
            email = form.cleaned_data['email']
            EmailMessage(
               'Scholarship Application Form Submission from {}'.format(first_name),
               last_name,
               'imperialCollege@example.com', # Send from (your website)
               ['josephayemlo@gmail.com'], # Send to (your admin email)
               [],
               reply_to=[email] # Email from the form to get back to
           ).send()
            EmailMessage(
               'Your scholarship application has been recieved sucessfuly {}'.format(first_name),
               last_name,
               'imperialCollege@example.com', # Send from (your website)
               [email], # Send to (your admin email)
               [],
               reply_to=[email] # Email from the form to get back to

              
           ).send()

            return redirect('success')
    else:
        form = ScholarshipApplicationForm()
    return render(request, 'core/apply_scholarship.html', {'form': form })




# UG application form view

def undergraduate_Application_Form_View(request):
    if request.method == 'POST':
        form = UndergraduateApplicationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')

            # Check if email is already in use
            if CustomUser.objects.filter(email=email).exists():
                form.add_error('email', 'This email is already registered.')
                messages.error(request, "This email is already registered.")
                return render(request, 'core/undergraduate_application_form.html', {'form': form})

            try:
                with transaction.atomic():
                    # Extract cleaned data
                    first_name = form.cleaned_data.get('first_name')
                    last_name = form.cleaned_data.get('last_name')
                    address_1 = form.cleaned_data.get('address_1')
                    phone_number = form.cleaned_data.get('phone_number')
                    gender = form.cleaned_data.get('gender')
                    course_of_study = form.cleaned_data.get('course_of_study')

                    # Generate custom password
                    custom_password = first_name.lower() + str(random.randint(1000, 9999))

                    # Save application instance without committing to DB yet
                    application = form.save(commit=False)

                    # Create user
                    user = CustomUser.objects.create_user(
                        email=email,
                        password=custom_password,
                        first_name=first_name,
                        last_name=last_name,
                        user_type=5,
                        gender=gender,
                        address=address_1
                    )

                    # Create Aspirant profile
                    AspirantStudent.objects.create(
                        admin=user,
                        course_applied=course_of_study,
                        phone_number=phone_number,
                        address_1=application.address_1,
                        address_2=application.address_2,
                        city=application.city,
                        state_province=application.state_province,
                        postal_code=application.postal_code,
                        country=application.country
                    )

                    # Save application to DB
                    application.save()

                    # Send emails
                    EmailMessage(
                        subject='[Notice] New UG Application Received',
                        body=f"""
Undergraduate Application Form Submission

Name: {first_name} {last_name}
Email: {email}
Course Applied: {course_of_study}
                        """,
                        from_email='no-reply@imperialCollege.edu',
                        to=['josephayemlojay@gmail.com'],
                        reply_to=[email]
                    ).send()

                    EmailMessage(
                        subject=f'Welcome to Imperial College, {first_name}',
                        body=f"""
Dear {first_name},

Thank you for applying to Imperial College.

Your application has been received successfully.

Please log in to your Aspirant Portal and complete your profile.

🔐 Login Credentials:
Email: {email}
Password: {custom_password}

Use the above credentials at: https://imperialcollege.edu/aspirant-login

Best regards,
Imperial College Admissions
                        """,
                        from_email='no-reply@imperialCollege.edu',
                        to=[email]
                    ).send()

                print("All operations succeeded")
                return redirect('success')

            except Exception as e:
                messages.error(request, "An unexpected error occurred: " + str(e))
                # At this point, all DB changes are rolled back
                return render(request, 'core/undergraduate_application_form.html', {'form': form})

    else:
        form = UndergraduateApplicationForm()

    return render(request, 'core/undergraduate_application_form.html', {'form': form})

def success(request):
    return render(request, 'core/success.html')