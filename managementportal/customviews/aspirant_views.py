from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import update_session_auth_hash
from core.models import AspirantStudent
from core.forms import AspirantStudentForm
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

# Create your views here.
# add
def add_aspirant(request):
    form = AspirantStudentForm(request.POST or None, request.FILES or None)
    context = {'form': form, 'page_title': 'Add Aspirant'}

    if request.method == 'POST':
        if form.is_valid():
            # User fields
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            address = form.cleaned_data.get('address')
            email = form.cleaned_data.get('email')
            gender = form.cleaned_data.get('gender')
            password = form.cleaned_data.get('password')

            try:
                # Create user with all fields at once
                user = User.objects.create_user(
                    email=email,
                    password=password,
                    user_type=5,
                    first_name=first_name,
                    last_name=last_name,
                    gender=gender,
                    address=address
                )
                # Manually create Aspirant object
                aspirant = AspirantStudent.objects.create(
                    admin=user, #Aspirant should fill the rest data or admin use edit to complete the profile data
                )
                messages.success(request, "Aspirant successfully added.")
                return redirect(request.path)
            except Exception as e:
                messages.error(request, "Could not add student: " + str(e))
        else:
            messages.error(request, "Please fill all required fields correctly.")
    return render(request, 'management/partials/aspirant/add_aspirant.html', context)



def manage_aspirant(request):
    aspirants = AspirantStudent.objects.select_related('admin').order_by('admin__last_name')
    return render(request, 'management/partials/aspirant/manage_aspirant.html', {'aspirants': aspirants})



def edit_aspirant(request, aspirant_id):
    aspirant = get_object_or_404(AspirantStudent, id=aspirant_id)
    user = aspirant.admin  # linked User object
    form = AspirantStudentForm(request.POST or None, instance=aspirant)

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

                # Extra Fields fort Aspirant
                aspirant.course_applied = form.cleaned_data['course_applied']
                aspirant.phone_number = form.cleaned_data['phone_number']
                aspirant.address_1 = form.cleaned_data['address_1']
                aspirant.address_2 = form.cleaned_data['address_2']
                aspirant.city = form.cleaned_data['city']
                aspirant.state_province = form.cleaned_data['state_province']
                aspirant.postal_code = form.cleaned_data['postal_code']
                aspirant.country = form.cleaned_data['country']

                # Educational
                aspirant.school_name = form.cleaned_data['school_name']
                aspirant.school_address_1 = form.cleaned_data['school_address_1']
                aspirant.school_address_2 = form.cleaned_data['school_address_2']
                aspirant.school_city = form.cleaned_data['school_city']
                aspirant.school_state_province = form.cleaned_data['school_state_province']
                aspirant.school_postal_code = form.cleaned_data['school_postal_code']
                aspirant.school_year_graduated = form.cleaned_data['school_year_graduated']

                # Emergency
                aspirant.emergency_first_name = form.cleaned_data['emergency_first_name']
                aspirant.emergency_last_name = form.cleaned_data['emergency_last_name']
                aspirant.emergency_email = form.cleaned_data['emergency_email']
                aspirant.emergency_phone_number = form.cleaned_data['emergency_phone_number']
                aspirant.emergency_address_1 = form.cleaned_data['emergency_address_1']
                aspirant.emergency_address_2 = form.cleaned_data['emergency_address_2']
                aspirant.emergency_city = form.cleaned_data['emergency_city']
                aspirant.emergency_postal_code = form.cleaned_data['emergency_postal_code']
                aspirant.emergency_country = form.cleaned_data['emergency_country']
                aspirant.emergency_relationship = form.cleaned_data['emergency_relationship']

                # Referee
                aspirant.referee_first_name = form.cleaned_data['referee_first_name']
                aspirant.referee_last_name = form.cleaned_data['referee_last_name']
                aspirant.referee_email = form.cleaned_data['referee_email']
                aspirant.referee_phone_number = form.cleaned_data['referee_phone_number']
                aspirant.referee_address_1 = form.cleaned_data['referee_address_1']
                aspirant.referee_address_2 = form.cleaned_data['referee_address_2']
                aspirant.referee_city = form.cleaned_data['referee_city']
                aspirant.referee_postal_code = form.cleaned_data['referee_postal_code']
                aspirant.referee_state_province = form.cleaned_data['referee_state_province']
                aspirant.referee_country = form.cleaned_data['referee_country']

                # Admission
                aspirant.admission_status = form.cleaned_data['admission_status']

                # Session
                aspirant.session = form.cleaned_data['session']
                
                aspirant.save()
                messages.success(request, "Successfully updated Aspirant.")
                return redirect(request.path)
            
            except Exception as e:
                messages.error(request, f"Could not update Aspirant: {e}")
        else:
            messages.error(request, "Please fill out the form correctly.")

    context = {
        'form': form,
        'aspirant': aspirant,
        'page_title': 'Edit aspirant'
    }
    return render(request, "management/partials/aspirant/edit_aspirant.html", context)
# delete
def delete_aspirant(request, aspirant_id):
    if request.method == 'POST':
        aspirant = get_object_or_404(AspirantStudent, id=aspirant_id)
        aspirant.delete()
        messages.success(request, 'aspirant Deleted Sucessfully')
        return render(request,'management/partials/success.html')
    return render(request, 'management/partials/aspirant/manage_aspirant.html')
    