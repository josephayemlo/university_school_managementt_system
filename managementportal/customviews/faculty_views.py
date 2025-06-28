from django.shortcuts import render, redirect
from core.forms import *
from django.contrib import messages
from ..forms import FacultyForm

# Create your views here.

def add_faculty(request):
    form = FacultyForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "Faculty added successfully.")
        return redirect('management_home')
    return render(request, 'core/add_faculty.html', {'form': form})


