from django.shortcuts import render,redirect,  get_object_or_404
from accounts.forms import AspirantStudentForm 
from studentportal.models import AspirantStudent
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import update_session_auth_hash
from core.models import *
from .models import *
from .forms import *
# Create your views here.

def course_registration(request):
    return render (request, 'student/course_registration.html')

def student_available_course(request):
    student = get_object_or_404(Student, admin=request.user)

    current_calendar = AcademicCalendar.objects.get(is_current=True)

    courses = LevelCourse.objects.filter(
        level=student.level,
        semester=current_calendar.semester,
        course_of_study=student.course_of_study
    ).select_related('course')

    return render(request, 'student/student_available_course.html', {
        'student': student,
        'courses': courses,
        'semester': current_calendar.semester,
    })


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
            return redirect('student_available_course')
    else:
         # GET request – preselect previously registered courses
        previously_registered_courses = RegisteredCourse.objects.filter(
        student=student,
        academic_calendar=current_calendar
        ).values_list('course_id', flat=True)

        form = CourseRegistrationForm(
            available_courses=available_courses,
            initial={'courses': previously_registered_courses}
        )

    return render(request, 'student/register_courses.html', {
        'form': form,
        'student': student,
        'semester': current_calendar.semester,
    })


def student_home (request):
    return render(request, 'student_home.html')


def aspirant_student_home (request):
    return render(request, 'aspirant_student_home.html')


def edit_aspirant_student(request):
  
    aspirantstudent = get_object_or_404(AspirantStudent, admin=request.user)
    form = AspirantStudentForm(request.POST or None, instance=aspirantstudent)
    context = {
        'form': form,
        'page_title': 'Edit Aspirant Student',
    }
    print('context is valid')

    if request.method == 'POST':
        try:
            if form.is_valid():
                # Save CustomUser info
                admin = aspirantstudent.admin
                admin.first_name = form.cleaned_data.get('first_name')
                admin.last_name = form.cleaned_data.get('last_name')
                admin.address = form.cleaned_data.get('address')
                admin.gender = form.cleaned_data.get('gender')
                password = form.cleaned_data.get('password')
                if password:
                    admin.set_password(password)
                    update_session_auth_hash(request, admin)   # ✅ Re-authenticate the session 
                    # if you dont re_authenticate the user, 
                
                admin.save()

                # Save AspirantStudent info
                form.save()

                messages.success(request, "Profile Updated!")
                return redirect(reverse('edit_aspirant_student'))
            else:
                print("Errors:", form.errors.as_json())
                messages.error(request, "Invalid data provided.")
        except Exception as e:
            messages.error(request, "Error occurred while updating profile: " + str(e))

    return render(request, "student/edit_aspirant_student_template.html", context)