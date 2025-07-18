import mimetypes
import os
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.http.response import HttpResponse
from django.conf import settings
from django.contrib import messages
import random
from django.db import transaction
from core.models import AspirantStudent
from django.contrib.auth import get_user_model
User = get_user_model()
from .forms import UndergraduateApplicationForm, ScholarshipApplicationForm
# Create your views here.

# apply home view
def apply (request):
    return render(request, 'applications/apply.html')

# UG apply view
def apply_Undergraduate (request):
    return render(request, 'applications/apply_undergraduate.html')

# UG apply process
def apply_Undergraduate_Process (request):
    file_name = 'personal_statement/Writing-a-Personal-Statement.pdf'
    file_stats = os.stat(os.path.join(settings.MEDIA_ROOT, file_name))
    file_size = file_stats.st_size
    context={
        'file_size': file_size,
        'file_name': file_name
    }
    return render(request, 'applications/apply_undergraduate_process.html', context)

# PG apply view
def apply_Postgraduate (request):
    return render(request, 'applications/apply_postgraduate.html')

# personal statement download
def personal_statement_download(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = 'Writing-a-Personal-Statement.pdf'
    filepath = BASE_DIR + '/media/personal_statement/' + filename
    path = open(filepath, 'rb')
    mime_type, _ = mimetypes.guess_type(filepath)
    response = HttpResponse(path, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response

# UG application form view
def undergraduate_Application_Form_View(request):
    if request.method == 'POST':
        form = UndergraduateApplicationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            # Check if email is already in use
            if User.objects.filter(email=email).exists():
                form.add_error('email', 'This email is already registered.')
                messages.error(request, "This email is already registered.")
                return render(request, 'applications/undergraduate_application_form.html', {'form': form})
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
                    user = User.objects.create_user(
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
                        from_email='no-reply@CommunityCollege.edu',
                        to=['josephayemlojay@gmail.com'],
                        reply_to=[email]
                    ).send()

                    EmailMessage(
                        subject=f'Welcome to Community College, {first_name}',
                        body=f"""
Dear {first_name},

Thank you for applying to Community College USA.

Your application has been received successfully.

Please log in to your Aspirant Portal and complete your profile.

🔐 Login Credentials:
Email: {email}
Password: {custom_password}

Use the above credentials at: https://Communitycollege.edu/aspirant-login

Best regards,
Community College Admissions
                        """,
                        from_email='no-reply@CommunityCollege.edu',
                        to=[email]
                    ).send()
                messages.success(request, "Registeration Successful, check your email for further instructions.")
                return redirect('success')

            except Exception as e:
                messages.error(request, "An unexpected error occurred: " + str(e))
                # At this point, all DB changes are rolled back
                return render(request, 'applications/undergraduate_application_form.html', {'form': form})

    else:
        form = UndergraduateApplicationForm()

    return render(request, 'applications/undergraduate_application_form.html', {'form': form})


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
               'CommunityCollege@example.com', # Send from (your website)
               ['josephayemlo@gmail.com'], # Send to (your admin email)
               [],
               reply_to=[email] # Email from the form to get back to
           ).send()
            EmailMessage(
               'Your scholarship application has been recieved sucessfuly {}'.format(first_name),
               last_name,
               'CommunityCollege@example.com', # Send from (your website)
               [email], # Send to (your admin email)
               [],
               reply_to=[email] # Email from the form to get back to

              
           ).send()

            return redirect('success')
    else:
        form = ScholarshipApplicationForm()
    return render(request, 'applications/apply_scholarship.html', {'form': form })


def success(request):
    return render(request, 'applications/success.html')
