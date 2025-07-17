from core.forms import StudentResultForm
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from core.models import Department, AcademicCalendar, Course, RegisteredCourse, StudentResult, SemesterResult


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
            prefix = f"reg_{reg.id}_"
            ca1 = request.POST.get(prefix + 'ca1', 0) or 0
            ca2 = request.POST.get(prefix + 'ca2', 0) or 0
            ca3 = request.POST.get(prefix + 'ca3', 0) or 0
            exam = request.POST.get(prefix + 'exam', 0) or 0

            # 🔹 Ensure semester result exists
            semester_result, _ = SemesterResult.objects.get_or_create(
                student=reg.student,
                academic_calendar=calendar
            )

            # 🔹 Save result and link it
            result, _ = StudentResult.objects.get_or_create(registered_course=reg)
            result.ca1 = ca1
            result.ca2 = ca2
            result.ca3 = ca3
            result.exam = exam
            result.updated_by = request.user
            result.semester_result = semester_result
            result.save()

            # Optional: semester_result.compute_result()  # can be called later

        messages.success(request, "Results saved successfully.")
        return redirect(request.path)

    context = {
        'course': course,
        'calendar': calendar,
        'registrations': registrations,
    }
    return render(request, 'management/partials/studentresult/result_registeredcourse_students.html', context)


def semester_result(request):
    return render(request, 'management/partials/studentresult/semester_result.html')
     

def semester_results_list(request):
    results = SemesterResult.objects.select_related('student', 'academic_calendar').all()

    # Optional filtering
    calendar_id = request.GET.get('calendar')
    if calendar_id:
        results = results.filter(academic_calendar_id=calendar_id)

    context = {
        'results': results,
        'calendars': AcademicCalendar.objects.all()
    }
    return render(request, 'management/partials/studentresult/semester_result_list.html', context)



def compute_semester_result_individual(request, result_id):
    result = get_object_or_404(SemesterResult, id=result_id)
    result.compute_result()

    messages.success(request, f"Computed GPA/CGPA for {result.student} - {result.academic_calendar}")
    return redirect('admin_semester_results_list')

def compute_all_semester_results_dashboard(request):
    return render(request, 'management/partials/studentresult/compute_all_semester_result.html')

def compute_all_semester_results(request):
    calendar = AcademicCalendar.objects.filter(is_current=True).first()

    if not calendar:
        messages.error(request, "No current academic calendar found.")
        return redirect('admin_semester_results_list')

    results = SemesterResult.objects.filter(academic_calendar=calendar)

    count = 0
    for result in results:
        result.compute_result()
        count += 1

    messages.success(request, f"{count} semester result(s) successfully computed.")
    return redirect('admin_compute_all_semester_results_dashboard')

def compute_by_department(request):
    calendar = AcademicCalendar.objects.filter(is_current=True).first()

    if not calendar:
        messages.error(request, "No current academic calendar set.")
        return redirect('semester_results_list')

    departments = Department.objects.all()

    if request.method == 'POST':
        dept_id = request.POST.get('department')
        if not dept_id:
            messages.error(request, "Please select a department.")
            return redirect('compute_by_department')

        department = get_object_or_404(Department, id=dept_id)

        results = SemesterResult.objects.filter(
            academic_calendar=calendar,
            student__course_of_study__department=department
        ).select_related('student')

        count = 0
        for result in results:
            result.compute_result()
            count += 1

        messages.success(request, f"{count} results computed for {department.name}.")
        print('Computed')
        return redirect(request.path)

    context = {
        'departments': departments,
    }
    return render(request, 'management/partials/studentresult/compute_by_department.html', context)


def release_by_department(request):
    calendar = AcademicCalendar.objects.filter(is_current=True).first()

    if not calendar:
        messages.error(request, "No current academic calendar set.")
        return redirect('admin_result_and_assessment')

    departments = Department.objects.all()

    if request.method == 'POST':
        dept_id = request.POST.get('department')
        if not dept_id:
            messages.error(request, "Please select a department.")
            return redirect('release_by_department')

        department = get_object_or_404(Department, id=dept_id)

        results = SemesterResult.objects.filter(
            academic_calendar=calendar,
            student__course_of_study__department=department,
            is_released=False
        )

        count = results.count()
        results.update(is_released=True)

        messages.success(request, f"{count} results released for {department.name}.")
        return redirect(request.path)

    context = {
        'departments': departments,
    }
    return render(request, 'management/partials/studentresult/release_by_department.html', context)




def release_all_results_dashboard(request):
    return render(request, 'management/partials/studentresult/release_all_results_dashboard.html')


def release_all_results(request):
    calendar = AcademicCalendar.objects.filter(is_current=True).first()

    if not calendar:
        messages.error(request, "No current academic calendar set.")
        return redirect('admin_result_and_assessment')

    results = SemesterResult.objects.filter(
        academic_calendar=calendar,
        is_released=False
    )

    count = results.count()
    results.update(is_released=True)
    messages.success(request, f"{count} semester results released.")
    return redirect('admin_release_all_results_dashboard')


def unrelease_all_results(request):
    calendar = AcademicCalendar.objects.filter(is_current=True).first()

    if not calendar:
        messages.error(request, "No current academic calendar set.")
        return redirect('admin_result_and_assessment')

    results = SemesterResult.objects.filter(
        academic_calendar=calendar,
        is_released=True
    )

    count = results.count()
    results.update(is_released=False)
    messages.success(request, f"{count} semester results unreleased.")
    return redirect('admin_release_all_results_dashboard')
