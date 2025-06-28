from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from core.models import LevelCourse
from ..forms import LevelCourseForm

# assign
def assign_level_course(request):
    if request.method == 'POST':
        form = LevelCourseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Course Assigned to Level Sucessfully')
            return render(request,'management/partials/success.html')
    else:
        form = LevelCourseForm()
    return render(request, 'management/partials/levelcourse/assign_course_to_level.html', {'form':form})

# manage/view
def manage_level_course(request):
    levelcourse = LevelCourse.objects.all()
    context= {"levelcourse":levelcourse}
    return render(request, 'management/partials/levelcourse/manage_level_course.html', context)

# edit
def edit_level_course(request, course_id):
    levelcourse = get_object_or_404(LevelCourse, id=course_id)
    if request.method == 'POST':
        form = LevelCourseForm(request.POST, instance=levelcourse)
        if form.is_valid():
            form.save()
            messages.success(request, 'Level Course Updated Sucessfully')
            return render(request,'management/partials/success.html')
    else:
        form = LevelCourseForm(instance=levelcourse)
    context = {
        "form": form,
        "levelcourse": levelcourse
    }
    return render(request, 'management/partials/levelcourse/edit_level_course.html', context)


# delete
def delete_level_course(request, course_id):
    if request.method == 'POST':
        levelcourse = get_object_or_404(LevelCourse, id=course_id)
        levelcourse.delete()
        messages.success(request, 'Level Course Deleted Sucessfully')
        return render(request,'management/partials/success.html')
    return render(request, 'management/partials/levelcourse/manage_level_course.html')
    

