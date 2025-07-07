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


# this is bad structure
def aspirant_student_list(request):
    aspirantstudents = User.objects.filter(user_type=5)
    return render(request, 'management/partials/aspirant/aspirant_student_list.html', {'aspirantstudents': aspirantstudents})

