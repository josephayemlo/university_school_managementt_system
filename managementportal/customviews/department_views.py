from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from ..forms import DepartmentForm

# Views
def add_department(request):
    form = DepartmentForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "Department added successfully.")
        return redirect('management_home')
    return render(request, 'core/add_department.html', {'form': form})