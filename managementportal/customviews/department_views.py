from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from ..forms import DepartmentForm
from core.models import Department
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

# permission check
def is_custom_superuser(user):
    return user.is_authenticated and user.user_type == '1'


# Add
@login_required
@user_passes_test(is_custom_superuser)
def add_department(request):
    form = DepartmentForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "Department added successfully.")
        return redirect(request.path)
    return render(request, 'management/partials/department/add_department.html', {'form': form})

# manage/view
@login_required
@user_passes_test(is_custom_superuser)
def manage_department(request):
    department = Department.objects.all()
    context= {"department":department}
    return render(request, 'management/partials/department/manage_department.html', context)


# edit
@login_required
@user_passes_test(is_custom_superuser)
def edit_department(request, department_id):
    department = get_object_or_404(Department, id=department_id)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            messages.success(request, 'department Updated Sucessfully')
            return redirect(request.path)
        
    else:
        form = DepartmentForm(instance=department)
    context = {
        "form": form,
        "department": department
    }

    return render(request, 'management/partials/department/edit_department.html', context)

# delete
@login_required
@user_passes_test(is_custom_superuser)
def delete_department(request, department_id):
    if request.method == 'POST':
        department = get_object_or_404(Department, id=department_id)
        department.delete()
        print("department deleted")
        messages.success(request, 'department Deleted Sucessfully')
        return render(request,'management/partials/success.html')
    return render(request, 'management/partials/department/manage_department.html')
    

