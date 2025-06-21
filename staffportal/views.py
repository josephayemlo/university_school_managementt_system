from django.shortcuts import render

# Create your views here.


def academicstaff_home (request):
    return render(request, 'academicstaff_home.html')


def nonacademicstaff_home (request):
    return render(request, 'nonacademicstaff_home.html')
