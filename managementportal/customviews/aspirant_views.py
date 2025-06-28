from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import update_session_auth_hash

from core.forms import AspirantStudentForm
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

# Create your views here.

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
                user = User.objects.create_user(
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

    return render(request, 'management/partials/aspirant/add_aspirant_student_template.html', context)



def aspirant_student_list(request):
    aspirantstudents = User.objects.filter(user_type=5)
    return render(request, 'management/partials/aspirant/aspirant_student_list.html', {'aspirantstudents': aspirantstudents})


# # Aspirant Self-Edit View 
# def edit_aspirant_student(request):
  
#     aspirantstudent = get_object_or_404(AspirantStudent, admin=request.user)
#     form = AspirantStudentForm(request.POST or None, instance=aspirantstudent)
#     context = {
#         'form': form,
#         'page_title': 'Edit Aspirant Student',
#     }
#     print('context is valid')

#     if request.method == 'POST':
#         try:
#             if form.is_valid():
#                 # Save User info
#                 admin = aspirantstudent.admin
#                 admin.first_name = form.cleaned_data.get('first_name')
#                 admin.last_name = form.cleaned_data.get('last_name')
#                 admin.address = form.cleaned_data.get('address')
#                 admin.gender = form.cleaned_data.get('gender')
#                 password = form.cleaned_data.get('password')
#                 if password:
#                     admin.set_password(password)
#                     update_session_auth_hash(request, admin)   # ✅ Re-authenticate the session 
#                     # if you dont re_authenticate the user, 
                
#                 admin.save()

#                 # Save AspirantStudent info
#                 form.save()

#                 messages.success(request, "Profile Updated!")
#                 return redirect(reverse('edit_aspirant_student'))
#             else:
#                 print("Errors:", form.errors.as_json())
#                 messages.error(request, "Invalid data provided.")
#         except Exception as e:
#             messages.error(request, "Error occurred while updating profile: " + str(e))

#     return render(request, "student/edit_aspirant_student_template.html", context)
