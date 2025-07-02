from core.forms import StudentResultForm
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from core.models import Department, AcademicCalendar, Course, RegisteredCourse, StudentResult


def result_select_department(request):
    department = Department.objects.all()
    context = {
        'department': department
    }
    return render(request, 'management/partials/studentresult/result_select_department.html', context)


def result_department_course(request, department_id ):
    department = get_object_or_404(Department, id=department_id)
    current_calendar = AcademicCalendar.objects.filter(is_current=True).first()
    if not current_calendar:
            return render(request, 'management/partials/studentresult/no_current_calendar.html')

        # Get all registered courses under this department for current session/semester
    registered_courses = RegisteredCourse.objects.filter(
        course__department=department,
        academic_calendar=current_calendar
    ).select_related('course').distinct()

    # Get unique course instances (so one course is not listed multiple times)
    unique_courses = Course.objects.filter(
        id__in=registered_courses.values_list('course_id', flat=True)
    )

    context = {
        'department': department,
        'courses': unique_courses,
        'current_calendar': current_calendar,
    }
    return render(request, 'management/partials/studentresult/result_department_course.html', context)



# working on

def result_registeredcourse_students(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    calendar = AcademicCalendar.objects.filter(is_current=True).first()
    print ('course and calender loaded')

    if not calendar:
        messages.error(request, "No current academic calendar is set.")
        return redirect('result_select_department')

    registrations = RegisteredCourse.objects.filter(
        course=course,
        academic_calendar=calendar,
        approved=True
    ).select_related('student')

    if request.method == 'POST':
        for reg in registrations:
            # Get score values from POST data
            prefix = f"reg_{reg.id}_"
            ca1 = request.POST.get(prefix + 'ca1', 0) or 0
            ca2 = request.POST.get(prefix + 'ca2', 0) or 0
            ca3 = request.POST.get(prefix + 'ca3', 0) or 0
            exam = request.POST.get(prefix + 'exam', 0) or 0

            # Save or update result
            result, created = StudentResult.objects.get_or_create(registered_course=reg)
            result.ca1 = ca1
            result.ca2 = ca2
            result.ca3 = ca3
            result.exam = exam
            result.updated_by = request.user
            result.save()
            print ('result saved')

        messages.success(request, "Results saved successfully.")
        return redirect(request.path)  # reload the same page

    context = {
        'course': course,
        'calendar': calendar,
        'registrations': registrations,
    }
    return render(request, 'management/partials/studentresult/result_registeredcourse_students.html', context)









