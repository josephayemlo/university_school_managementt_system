from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render

def nonacademicstaff_home (request):
    return render(request, 'staff/nonacademicstaff/nonacademicstaff_home.html')

def addmissions_ (request):
    return render(request, 'staff/nonacademicstaff/nonacademicstaff_home.html')
