from django.shortcuts import render, redirect
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
from .forms import FacultyForm, DepartmentForm, CourseOfStudyForm
from django.contrib import messages
from studentportal.models import AspirantStudent
import random
from django.db import transaction



def add_faculty(request):
    form = FacultyForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "Faculty added successfully.")
        return redirect('management_home')
    return render(request, 'core/add_faculty.html', {'form': form})

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
        return redirect('management_home')
    return render(request, 'core/add_course_of_study.html', {'form': form})

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