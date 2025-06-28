from django.shortcuts import render, redirect
from django.http import HttpResponse
from .EmailBackend import EmailBackend
from django.contrib import messages
from django.contrib.auth import login, logout
from django.urls import reverse
from django.http.response import HttpResponse
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.


# success
def success(request):
    return render(request, 'core/success.html')

def login_page (request):
    if request.user.is_authenticated:
        if request.user.user_type == '1':
            return redirect(reverse("management_home"))
        elif request.user.user_type == '2':
            return redirect(reverse("academicstaff_home"))
        elif request.user.user_type == '3':
            return redirect(reverse("nonacademicstaff_home"))
        elif request.user.user_type == '4':
            return redirect(reverse("student_portal"))
        else:
            return redirect(reverse("aspirant_student_home"))
    return render(request, 'accounts/login.html')

def login_user(request, **kwargs):
    if request.method != 'POST':
        return HttpResponse("<h4>Denied</h4>")
    else:
        user = EmailBackend.authenticate(request, username=request.POST.get('email'), password=request.POST.get('password'))
        if user != None:
            login(request, user)
            if request.user.user_type == '1':
                return redirect(reverse("management_home"))
            elif request.user.user_type == '2':
                return redirect(reverse("academicstaff_home"))
            elif request.user.user_type == '3':
                return redirect(reverse("nonacademicstaff_home"))
            elif request.user.user_type == '4':
                return redirect(reverse("student_portal"))
            else:
                return redirect(reverse("aspirant_student_home"))
        else:
            messages.error(request, "Invalid details")
            return redirect("login_page")
        
def logout_user(request):
    if request.user != None:
        logout(request)
    return redirect("/")

