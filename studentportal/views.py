from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from itertools import groupby
from .forms import CourseRegistrationForm
from core.models import AcademicCalendar, RegisteredCourse, Course, LevelCourse, Student
from django.contrib.auth import update_session_auth_hash
from .forms import StudentProfileForm
from django.urls import reverse
from core.models import SemesterResult, StudentResult
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

    
def is_student(user):
    return user.is_authenticated and user.user_type == '4'


# Student Portal home
@login_required
@user_passes_test(is_student)
def student_portal (request):
    student = request.user.student
    context= {
        'student': student,
        'student_level': student.level,
        'study_duration': student.course_of_study.duration_years

    }
    
    return render(request, 'studentportal/student_portal.html', context)



@login_required
@user_passes_test(is_student)
def edit_student(request):
    student = get_object_or_404(Student, admin=request.user)
    form = StudentProfileForm(request.POST or None, instance=student)
    context = {
        'form': form,
    }
    if request.method == 'POST':
        try:
            if form.is_valid():
                # Save User info
                admin = student.admin
                admin.first_name = form.cleaned_data.get('first_name')
                admin.last_name = form.cleaned_data.get('last_name')
                admin.address = form.cleaned_data.get('address')
                admin.gender = form.cleaned_data.get('gender')
                password = form.cleaned_data.get('password')
                if password:
                    admin.set_password(password)
                    update_session_auth_hash(request, admin)   #Re-authenticate the session 
                admin.save()
                form.save()
                messages.success(request, "Profile Updated!")
                return redirect(reverse('edit_student'))
            else:
                print("Errors:", form.errors.as_json())
                messages.error(request, "Invalid data provided.")
        except Exception as e:
            messages.error(request, "Error occurred while updating profile: " + str(e))

    return render(request, "studentportal/partials/edit_student.html", context)



# Previous Registered Courses
@login_required
@user_passes_test(is_student)
def previous_registered_courses(request):
    student = get_object_or_404(Student, admin=request.user)

    # Get all non-current academic calendars
    previous_calendars = AcademicCalendar.objects.filter(is_current=False)
    """
    We did not use .first() here because when it is false we expect a queryset(list) of 
    previous calender which in template we loop through. However when is_current=True
    we cant loop in template because we expect one object but since we knw filter always
    returns a queryset(list) we just use first() to select the first object 
    """

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

    return render(request, 'studentportal/partials/previous_registered_courses.html', {
        'grouped_registrations': grouped
    })

# previous registered courese details view
@login_required
@user_passes_test(is_student)
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

    return render(request, 'studentportal/partials/previous_registration_details.html', {
        'courses': courses,
        'level': level,
        'semester': semester,
    })


# Current Registered courses
@login_required
@user_passes_test(is_student)
def registered_courses(request):
    student = get_object_or_404(Student, admin=request.user)
    academic_calendar = AcademicCalendar.objects.get(is_current=True)
    registered_courses = RegisteredCourse.objects.filter(
        student=student,
        academic_calendar = academic_calendar
    )
    context = {
        'registered_courses':registered_courses,
        'academic_calendar':academic_calendar


    }
    return render (request, 'studentportal/partials/registered_courses.html',context)

# course registration
@login_required
@user_passes_test(is_student)
def course_registration(request):
    return render (request, 'studentportal/partials/course_registration.html')

# Current Semester Available courses
@login_required
@user_passes_test(is_student)
def student_available_course(request):
    student = get_object_or_404(Student, admin=request.user)
    current_calendar = AcademicCalendar.objects.get(is_current=True)
    courses = LevelCourse.objects.filter(
        level=student.level,
        semester=current_calendar.semester,
        course_of_study=student.course_of_study
    ).select_related('course')
    return render(request, 'studentportal/partials/student_available_course.html', {
        'student': student,
        'courses': courses,
        'semester': current_calendar.semester,
    })

# Register courses
@login_required
@user_passes_test(is_student)
def register_courses(request):
    student = get_object_or_404(Student, admin=request.user)
    current_calendar = AcademicCalendar.objects.get(is_current=True)

    # Get the courses relevant to the student's level, semester, and program
    level_courses = LevelCourse.objects.filter(
        level=student.level,
        semester=current_calendar.semester,
        course_of_study=student.course_of_study
    ).select_related('course')

    # Extract the actual course objects
    available_courses = Course.objects.filter(id__in=level_courses.values_list('course_id', flat=True))

    if request.method == 'POST':
        form = CourseRegistrationForm(request.POST, available_courses=available_courses)
        if form.is_valid():
            selected_courses = form.cleaned_data['courses']

            # Remove any previously registered courses for this session/semester
            RegisteredCourse.objects.filter(
                student=student,
                academic_calendar=current_calendar
            ).delete()

            # Save new course registrations
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
            return render(request, 'studentportal/partials/success.html')

    else:
        # Handle GET: preselect already registered courses
        previously_registered_courses = RegisteredCourse.objects.filter(
            student=student,
            academic_calendar=current_calendar
        ).values_list('course_id', flat=True)

        form = CourseRegistrationForm(
            available_courses=available_courses,
            initial={'courses': previously_registered_courses}
        )

    # Zip each checkbox field with the matching Course object
    course_fields = zip(form['courses'], available_courses)

    return render(request, 'studentportal/partials/register_courses.html', {
        'form': form,
        'student': student,
        'semester': current_calendar.semester,
        'course_fields': course_fields,
    })

@login_required
@user_passes_test(is_student)
def student_approved_result_dashboard (request):
    student = request.user.student  # adjust if you use OneToOne or a custom method
    released_results = SemesterResult.objects.filter(
        student=student,
        is_released=True
    ).select_related('academic_calendar').order_by('-academic_calendar__session')

    context = {
        'released_results': released_results,
    }
    return render(request, 'studentportal/partials/student_approved_result_dashboard.html', context)

@login_required
@user_passes_test(is_student)
def student_approved_result_details(request, result_id):
    student = request.user.student
    result = get_object_or_404(
        SemesterResult,
        id=result_id,
        student=student,
        is_released=True
    )

    detailed_results = StudentResult.objects.filter(
        semester_result=result
    ).select_related('registered_course__course')

    context = {
        'result': result,
        'detailed_results': detailed_results,
    }
    return render(request, 'studentportal/partials/student_approved_result_details.html', context)

