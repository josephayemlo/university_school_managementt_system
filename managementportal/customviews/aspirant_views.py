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
                # Manually create Student object
                aspirant = AspirantStudent.objects.create(
                    admin=user,
                )
                messages.success(request, "Aspirant successfully added.")
                return render(request,'management/partials/success.html')
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
    