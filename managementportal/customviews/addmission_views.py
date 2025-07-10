from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render
from core.models import AspirantStudent, AspirantAcademicCalendar, CourseOfStudy
from core.forms import AdmissionStatusForm



def addmissions (request):
    session = AspirantAcademicCalendar.objects.all()
    return render(request, 'management/partials/addmission/addmissions.html', {'session':session})

# list course applied
def admissions_courses(request, session_id):
    session = get_object_or_404(AspirantAcademicCalendar, id=session_id)
    
    # Get distinct courses that have applicants in this session
    courses = CourseOfStudy.objects.filter(
        aspirantstudent__session=session
    ).distinct()
    
    return render(request, 'management/partials/addmission/addmission_course.html', {
        'session': session,
        'courses': courses,
    })


# list applicants
def admissions_applicants(request, session_id, course_id):
    session = get_object_or_404(AspirantAcademicCalendar, id=session_id)
    course = get_object_or_404(CourseOfStudy, id=course_id)

    applicants = AspirantStudent.objects.filter(
        session=session,
        course_applied=course
    ).select_related('admin')  # Optional: faster if displaying user data

    return render(request, 'management/partials/addmission/addmission_applicants.html', {
        'session': session,
        'course': course,
        'applicants': applicants,
    })


def change_addmission_status(request, aspirant_id):
    aspirant = get_object_or_404(AspirantStudent, id=aspirant_id)
    form = AdmissionStatusForm(request.POST or None, instance=aspirant)
    if request.method == 'POST':
        if form.is_valid():
            # Admission
            aspirant.admission_status = form.cleaned_data['admission_status']
            aspirant.save()
            messages.success(request, "Successfully updated Addmision.")
            return redirect(request.path)
        else:
            messages.error(request, "Please fill out the form correctly.")
    context = {
        'form': form,
        'aspirant': aspirant,
    }
    return render(request, 'management/partials/addmission/change_addmission_status.html', context)
   
