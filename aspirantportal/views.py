from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import update_session_auth_hash
from .forms import AspirantStudentProfileForm
from core.models import AspirantStudent
from django.contrib import messages
from django.urls import reverse



# AspirantPortal Home
def aspirant_home (request):
    aspirant = request.user.aspirant
    return render(request, 'aspirantportal/aspirant_home.html', {'aspirant': aspirant})

# Aspirant Edit View 
def edit_aspirant(request):
  
    aspirantstudent = get_object_or_404(AspirantStudent, admin=request.user)
    form = AspirantStudentProfileForm(request.POST or None, instance=aspirantstudent)
    context = {
        'form': form,
        'page_title': 'Edit Aspirant Student',
    }
    print('context is valid')

    if request.method == 'POST':
        try:
            if form.is_valid():
                # Save User info
                admin = aspirantstudent.admin
                admin.first_name = form.cleaned_data.get('first_name')
                admin.last_name = form.cleaned_data.get('last_name')
                admin.address = form.cleaned_data.get('address')
                admin.gender = form.cleaned_data.get('gender')
                password = form.cleaned_data.get('password')
                if password:
                    admin.set_password(password)
                    update_session_auth_hash(request, admin)   # ✅ Re-authenticate the session 
                    # if you dont re_authenticate the user, 
                
                admin.save()

                # Save AspirantStudent info
                form.save()

                messages.success(request, "Profile Updated!")
                return redirect(reverse('edit_aspirant'))
            else:
                print("Errors:", form.errors.as_json())
                messages.error(request, "Invalid data provided.")
        except Exception as e:
            messages.error(request, "Error occurred while updating profile: " + str(e))

    return render(request, "aspirantportal/edit_aspirant.html", context)
