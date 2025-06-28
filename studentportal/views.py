from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from itertools import groupby
# Forms
from studentportal.forms import CourseRegistrationForm  
from managementportal.models import AcademicCalendar, RegisteredCourse, Course, LevelCourse
# Models
from studentportal.models import Student
    
# Create your views here.


# Student Portal home
def student_portal (request):
    return render(request, 'student/student_portal.html')

# Previous Registered Courses
def previous_registered_courses(request):
    student = get_object_or_404(Student, admin=request.user)

    # Get all non-current academic calendars
    previous_calendars = AcademicCalendar.objects.filter(is_current=False)

    # Fetch all courses registered in those sessions
    registered_courses = RegisteredCourse.objects.filter(
        student=student,
        academic_calendar__in=previous_calendars
    ).select_related('course', 'academic_calendar')

    # Sort for grouping: by level, then semester, then session
    registered_courses = sorted(
        registered_courses,
        key=lambda x: (
            x.course.level,
            x.academic_calendar.session,
            x.academic_calendar.semester
        )
    )
    # Group by (level, session, semester)
    grouped = []
    for key, group in groupby(registered_courses, key=lambda x: (
        x.course.level,
        x.academic_calendar.session,
        x.academic_calendar.semester
    )):
        level, session, semester = key
        group_list = list(group)
        grouped.append({
            'level': level,
            'session': session,
            'semester': semester,
            'timestamp': group_list[0].timestamp if group_list else None,
            'courses': group_list,
        })

    return render(request, 'student/partials/previous_registered_courses.html', {
        'grouped_registrations': grouped
    })

# previous registered courese details view
def previous_course_registration_details(request, level, semester):
    student = get_object_or_404(Student, admin=request.user)

    # Find the matching academic calendar with that session and semester
    academic_calendar = get_object_or_404(
        AcademicCalendar,
        semester=semester,
        is_current=False
    )
    # Get all registered courses that match level + semester + session
    courses = RegisteredCourse.objects.filter(
        student=student,
        academic_calendar=academic_calendar,
        course__level=level
    ).select_related('course')

    return render(request, 'student/partials/previous_registration_details.html', {
        'courses': courses,
        'level': level,
        'semester': semester,
    })


# Current Registered courses
def registered_courses(request):
    student = get_object_or_404(Student, admin=request.user)
    academic_calendar = AcademicCalendar.objects.get(is_current=True)
    registered_courses = RegisteredCourse.objects.filter(
        student=student,
        academic_calendar = academic_calendar
    )
    return render (request, 'student/partials/registered_courses.html', { 'registered_courses':registered_courses })

# course registration
def course_registration(request):
    return render (request, 'student/partials/course_registration.html')

# Current Semester Available courses
def student_available_course(request):
    student = get_object_or_404(Student, admin=request.user)
    current_calendar = AcademicCalendar.objects.get(is_current=True)
    courses = LevelCourse.objects.filter(
        level=student.level,
        semester=current_calendar.semester,
        course_of_study=student.course_of_study
    ).select_related('course')
    return render(request, 'student/partials/student_available_course.html', {
        'student': student,
        'courses': courses,
        'semester': current_calendar.semester,
    })

# Register courses
def register_courses(request):
    student = get_object_or_404(Student, admin=request.user)
    current_calendar = AcademicCalendar.objects.get(is_current=True)
    level_courses = LevelCourse.objects.filter(
        level=student.level,
        semester=current_calendar.semester,
        course_of_study=student.course_of_study
    ).select_related('course')

    available_courses = Course.objects.filter(id__in=level_courses.values_list('course_id', flat=True))

    if request.method == 'POST':
        form = CourseRegistrationForm(request.POST, available_courses=available_courses)
        if form.is_valid():
            selected_courses = form.cleaned_data['courses']

            # Remove any previously registered courses for this semester/session
            RegisteredCourse.objects.filter(
                student=student,
                academic_calendar=current_calendar
            ).delete()

            # Register new ones
            RegisteredCourse.objects.bulk_create([
                RegisteredCourse(
                    student=student,
                    course=course,
                    academic_calendar=current_calendar
                )
                for course in selected_courses
            ])

            messages.success(request, "Courses registered successfully.")
            print('course registered')
            # with redirect, django cannot redirct to a parital template so the best option is to return a rendered page
            return render(request, 'student/partials/success.html')
    else:
         # GET request – preselect previously registered courses
        previously_registered_courses = RegisteredCourse.objects.filter(
        student=student,
        academic_calendar=current_calendar
        ).values_list('course_id', flat=True) #this just allows us to get all id's of already registered course instead of returning the model

        form = CourseRegistrationForm(
            available_courses=available_courses,
            initial={'courses': previously_registered_courses}
        )

    return render(request, 'student/partials/register_courses.html', {
        'form': form,
        'student': student,
        'semester': current_calendar.semester,
    })


