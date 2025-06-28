from django.shortcuts import render, redirect
from accounts.forms import  CustomUser, AspirantStudentForm
from django.contrib import messages
from accounts.models import CustomUser
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



def aspirant_student_list(request):
    aspirantstudents = CustomUser.objects.filter(user_type=5)
    return render(request, 'student/aspirant_student_list.html', {'aspirantstudents': aspirantstudents})

