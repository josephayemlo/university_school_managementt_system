from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from core.models import AcademicCalendar, RegisteredCourse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test



# permission check
def is_custom_superuser(user):
    return user.is_authenticated and user.user_type == '1'

@login_required
@user_passes_test(is_custom_superuser)
def approve_all_course_reg_dashboard(request):
    return render(request, 'management/partials/coursereg/approve_all_course_reg_dashboard.html')


@login_required
@user_passes_test(is_custom_superuser)
def approve_all_course_reg(request):
    calendar = AcademicCalendar.objects.filter(is_current=True).first()

    if not calendar:
        messages.error(request, "No current academic calendar set.")
        return redirect('admin_student_course_registration')

    course_reg = RegisteredCourse.objects.filter(
        academic_calendar=calendar,
        approved=False
    )

    count = course_reg.count()
    course_reg.update(approved=True)
    messages.success(request, f"{count} semester course_reg approved.")
    return redirect('admin_approve_all_course_reg_dashboard')


@login_required
@user_passes_test(is_custom_superuser)
def unapprove_all_course_reg(request):
    calendar = AcademicCalendar.objects.filter(is_current=True).first()

    if not calendar:
        messages.error(request, "No current academic calendar set.")
        return redirect('admin_student_course_registration')

    course_reg = RegisteredCourse.objects.filter(
        academic_calendar=calendar,
        approved=True
    )

    count = course_reg.count()
    course_reg.update(approved=False)
    messages.success(request, f"{count} semester course_reg unapproved.")
    return redirect('admin_approve_all_course_reg_dashboard')
