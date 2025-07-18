from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from core.models import CourseOfStudy
from ..forms import CourseOfStudyForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

# permission check
def is_custom_superuser(user):
    return user.is_authenticated and user.user_type == '1'


# add
@login_required
@user_passes_test(is_custom_superuser)
def add_course_of_study(request):
    form = CourseOfStudyForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "Course of Study added successfully.")
        return redirect(request.path)
    return render(request, 'management/partials/courseofstudy/add_course_of_study.html', {'form': form})

# manage/view
@login_required
@user_passes_test(is_custom_superuser)
def manage_course_of_study(request):
    course_of_study = CourseOfStudy.objects.all()
    context= {"course_of_study":course_of_study}
    return render(request, 'management/partials/courseofstudy/manage_course_of_study.html', context)

# edit
@login_required
@user_passes_test(is_custom_superuser)
def edit_course_of_study(request, course_id):
    course_of_study = get_object_or_404(CourseOfStudy, id=course_id)
    if request.method == 'POST':
        form = CourseOfStudyForm(request.POST, instance=course_of_study)
        if form.is_valid():
            form.save()
            messages.success(request, 'Course of Study Updated Sucessfully')
            return redirect(request.path)
        
    else:
        form = CourseOfStudyForm(instance=course_of_study)
    context = {
        "form": form,
        "course_of_study": course_of_study
    }
    return render(request, 'management/partials/courseofstudy/edit_course_of_study.html', context)

# delete
@login_required
@user_passes_test(is_custom_superuser)
def delete_course_of_study(request, course_id):
    if request.method == 'POST':
        course_of_study = get_object_or_404(CourseOfStudy, id=course_id)
        course_of_study.delete()
        messages.success(request, 'Course of Study Deleted Sucessfully')
        return render(request,'management/partials/success.html')
    return render(request, 'management/partials/courseofstudy/manage_course_of_study.html')
    

