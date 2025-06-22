from django.shortcuts import render,redirect,  get_object_or_404
from accounts.forms import AspirantStudentForm 
from studentportal.models import AspirantStudent
from django.contrib import messages
from django.urls import reverse

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
    if request.method == 'POST':
        try:
            if form.is_valid():
                first_name = form.cleaned_data.get('first_name')
                last_name = form.cleaned_data.get('last_name')
                password = form.cleaned_data.get('password') or None
                address = form.cleaned_data.get('address')
                gender = form.cleaned_data.get('gender')
                admin = aspirantstudent.admin
                if password != None:
                    admin.set_password(password)
                admin.first_name = first_name
                admin.last_name = last_name
                admin.address = address
                admin.gender = gender
                admin.save()
                aspirantstudent.save()
                messages.success(request, "Profile Updated!")
                return redirect(reverse('edit_aspirant_student'))
            else:
                messages.error(request, "Invalid Data Provided")
        except Exception as e:
            messages.error(request, "Error Occured While Updating Profile " + str(e))
    return render(request, "student/edit_aspirant_student_template.html", context)
