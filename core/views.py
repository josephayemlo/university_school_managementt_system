from django.shortcuts import render

# Create your views here.

# home
def home (request):
    return render(request, 'core/home.html')

# student Public Home View
def student_home (request):
    return render(request, 'core/student_home.html')

# Aspirant Public Home
def aspirant_student_home (request):
    return render(request, 'core/aspirant_student_home.html')
