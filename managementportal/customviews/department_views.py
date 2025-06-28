from django.shortcuts import render, redirect
from django.contrib import messages
from ..forms import DepartmentForm

# Views
def add_department(request):
    form = DepartmentForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "Department added successfully.")
        return redirect('management_home')
    return render(request, 'management/partials/department/add_department.html', {'form': form})