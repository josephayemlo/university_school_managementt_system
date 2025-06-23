from django.shortcuts import render,redirect,  get_object_or_404
from accounts.forms import AspirantStudentForm 
from studentportal.models import AspirantStudent
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import update_session_auth_hash

# Create your views here.

def student_home (request):
    return render(request, 'student_home.html')


def aspirant_student_home (request):
    return render(request, 'aspirant_student_home.html')


def edit_aspirant_student(request):
  
    aspirantstudent = get_object_or_404(AspirantStudent, admin=request.user)
    form = AspirantStudentForm(request.POST or None, instance=aspirantstudent)
    context = {
        'form': form,
        'page_title': 'Edit Aspirant Student',
    }
    print('context is valid')

    if request.method == 'POST':
        try:
            if form.is_valid():
                # Save CustomUser info
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
                return redirect(reverse('edit_aspirant_student'))
            else:
                print("Errors:", form.errors.as_json())
                messages.error(request, "Invalid data provided.")
        except Exception as e:
            messages.error(request, "Error occurred while updating profile: " + str(e))

    return render(request, "student/edit_aspirant_student_template.html", context)