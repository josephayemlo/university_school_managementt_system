from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from core.models import Course
from ..forms import CourseForm

# add
def add_course(request):
    form = CourseForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Course added sucessfully')
        return render(request, 'management/partials/success.html')
    return render(request, 'management/partials/course/add_course.html', {'form': form})

# manage/view
def manage_course(request):
    course = Course.objects.all()
    context= {"course":course}
    return render(request, 'management/partials/course/manage_course.html', context)

# edit
def edit_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, 'Course Updated Sucessfully')
            return render(request,'management/partials/success.html')
    else:
        form = CourseForm(instance=course)
    context = {
        "form": form,
        "course": course
    }

    return render(request, 'management/partials/course/edit_course.html', context)

# delete
def delete_course(request, course_id):
    if request.method == 'POST':
        course = get_object_or_404(Course, id=course_id)
        course.delete()
        print("course deleted")
        messages.success(request, 'Course Deleted Sucessfully')
        return render(request,'management/partials/success.html')
    return render(request, 'management/partials/course/manage_course.html')
    

