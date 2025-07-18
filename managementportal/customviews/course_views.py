from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from core.models import Course
from ..forms import CourseForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

# permission check
def is_custom_superuser(user):
    return user.is_authenticated and user.user_type == '1'

# add
@login_required
@user_passes_test(is_custom_superuser)
def add_course(request):
    form = CourseForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Course added sucessfully')
        return redirect(request.path)
    return render(request, 'management/partials/course/add_course.html', {'form': form})

# manage/view
@login_required
@user_passes_test(is_custom_superuser)
def manage_course(request):
    course = Course.objects.all()
    context= {"course":course}
    return render(request, 'management/partials/course/manage_course.html', context)

# edit
@login_required
@user_passes_test(is_custom_superuser)
def edit_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, 'Course Updated Sucessfully')
            return redirect(request.path)
        
    else:
        form = CourseForm(instance=course)
    context = {
        "form": form,
        "course": course
    }

    return render(request, 'management/partials/course/edit_course.html', context)

# delete
@login_required
@user_passes_test(is_custom_superuser)
def delete_course(request, course_id):
    if request.method == 'POST':
        course = get_object_or_404(Course, id=course_id)
        course.delete()
        print("course deleted")
        messages.success(request, 'Course Deleted Sucessfully')
        return render(request,'management/partials/success.html')
    return render(request, 'management/partials/course/manage_course.html')
    

