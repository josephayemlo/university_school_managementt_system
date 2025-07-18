from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from core.models import LevelCourse
from ..forms import LevelCourseForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

# permission check
def is_custom_superuser(user):
    return user.is_authenticated and user.user_type == '1'

# assign
@login_required
@user_passes_test(is_custom_superuser)
def assign_level_course(request):
    if request.method == 'POST':
        form = LevelCourseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Course Assigned to Level Sucessfully')
            return redirect(request.path)
    else:
        form = LevelCourseForm()
    return render(request, 'management/partials/levelcourse/assign_course_to_level.html', {'form':form})

# manage/view
@login_required
@user_passes_test(is_custom_superuser)
def manage_level_course(request):
    levelcourse = LevelCourse.objects.all()
    context= {"levelcourse":levelcourse}
    return render(request, 'management/partials/levelcourse/manage_level_course.html', context)

# edit
@login_required
@user_passes_test(is_custom_superuser)
def edit_level_course(request, course_id):
    levelcourse = get_object_or_404(LevelCourse, id=course_id)
    if request.method == 'POST':
        form = LevelCourseForm(request.POST, instance=levelcourse)
        if form.is_valid():
            form.save()
            messages.success(request, 'Level Course Updated Sucessfully')
            return redirect(request.path)
    else:
        form = LevelCourseForm(instance=levelcourse)
    context = {
        "form": form,
        "levelcourse": levelcourse
    }
    return render(request, 'management/partials/levelcourse/edit_level_course.html', context)


# delete
@login_required
@user_passes_test(is_custom_superuser)
def delete_level_course(request, course_id):
    if request.method == 'POST':
        levelcourse = get_object_or_404(LevelCourse, id=course_id)
        levelcourse.delete()
        messages.success(request, 'Level Course Deleted Sucessfully')
        return render(request,'management/partials/success.html')
    return render(request, 'management/partials/levelcourse/manage_level_course.html')
    

