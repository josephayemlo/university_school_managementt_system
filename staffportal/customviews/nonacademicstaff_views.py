from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render
from core.models import AspirantStudent, AspirantAcademicCalendar, CourseOfStudy
from ..forms import AdmissionStatusForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

# permission check
def is_nonacd_staff(user):
    return user.is_authenticated and user.user_type == '3'


@login_required
@user_passes_test(is_nonacd_staff)
def nonacademicstaff_home (request):
    return render(request, 'staff/nonacademicstaff_home.html')

@login_required
@user_passes_test(is_nonacd_staff)
def addmissions (request):
    session = AspirantAcademicCalendar.objects.all()
    return render(request, 'staff/partials/nonacademicstaff/addmissions.html', {'session':session})

# list course applied
@login_required
@user_passes_test(is_nonacd_staff)
def addmissions_courses(request, session_id):
    session = get_object_or_404(AspirantAcademicCalendar, id=session_id)
    
    # Get distinct courses that have applicants in this session
    courses = CourseOfStudy.objects.filter(
        aspirantstudent__session=session
    ).distinct()
    
    return render(request, 'staff/partials/nonacademicstaff/addmission_course.html', {
        'session': session,
        'courses': courses,
    })


# list applicants
@login_required
@user_passes_test(is_nonacd_staff)
def addmissions_applicants(request, session_id, course_id):
    session = get_object_or_404(AspirantAcademicCalendar, id=session_id)
    course = get_object_or_404(CourseOfStudy, id=course_id)

    applicants = AspirantStudent.objects.filter(
        session=session,
        course_applied=course
    ).select_related('admin')  # Optional: faster if displaying user data

    return render(request, 'staff/partials/nonacademicstaff/addmission_applicants.html', {
        'session': session,
        'course': course,
        'applicants': applicants,
    })

@login_required
@user_passes_test(is_nonacd_staff)
def change_addmission_status(request, aspirant_id):
    aspirant = get_object_or_404(AspirantStudent, id=aspirant_id)
    form = AdmissionStatusForm(request.POST or None, instance=aspirant)
    if request.method == 'POST':
        if form.is_valid():
            # Admission
            aspirant.admission_status = form.cleaned_data['admission_status']
            aspirant.save()
            messages.success(request, "Successfully updated Addmision Great.")
            return redirect(request.path)
        else:
            messages.error(request, "Please fill out the form correctly.")
    context = {
        'form': form,
        'aspirant': aspirant,
    }
    return render(request, 'staff/partials/nonacademicstaff/change_addmission_status.html', context)
   
