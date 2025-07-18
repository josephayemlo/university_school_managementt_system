from django.shortcuts import render, redirect, get_object_or_404
from core.forms import *
from django.contrib import messages
from ..forms import FacultyForm
from core.models import Faculty
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

# permission check
def is_custom_superuser(user):
    return user.is_authenticated and user.user_type == '1'


# Add
@login_required
@user_passes_test(is_custom_superuser)
def add_faculty(request):
    form = FacultyForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "Faculty added successfully.")
        return redirect(request.path)
    return render(request, 'management/partials/faculty/add_faculty.html', {'form': form})



# manage/view
@login_required
@user_passes_test(is_custom_superuser)
def manage_faculty(request):
    faculty = Faculty.objects.all()
    context= {"faculty":faculty}
    return render(request, 'management/partials/faculty/manage_faculty.html', context)


# edit
@login_required
@user_passes_test(is_custom_superuser)
def edit_faculty(request, faculty_id):
    faculty = get_object_or_404(Faculty, id=faculty_id)
    if request.method == 'POST':
        form = FacultyForm(request.POST, instance=faculty)
        if form.is_valid():
            form.save()
            messages.success(request, 'faculty Updated Sucessfully')
            return redirect(request.path)
    else:
        form = FacultyForm(instance=faculty)
    context = {
        "form": form,
        "faculty": faculty
    }

    return render(request, 'management/partials/faculty/edit_faculty.html', context)

# delete
@login_required
@user_passes_test(is_custom_superuser)
def delete_faculty(request, faculty_id):
    if request.method == 'POST':
        faculty = get_object_or_404(Faculty, id=faculty_id)
        faculty.delete()
        print("faculty deleted")
        messages.success(request, 'faculty Deleted Sucessfully')
        return render(request,'management/partials/success.html')
    return render(request, 'management/partials/faculty/manage_faculty.html')
    

