from django.shortcuts import render
from core.models import AssignCourse, AcademicCalendar, Course, RegisteredCourse, StudentResult
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect



# Create your views here.

def result_upload(request, course_id):
    calendar = AcademicCalendar.objects.filter(is_current=True).first()
    if not calendar:
        messages.error(request, "No active academic calendar.")
        return redirect('academicstaff_home') 
    assigned_course = get_object_or_404(
        AssignCourse,
        academic_staff=request.user.academicstaff,
        course_id=course_id,
        academic_calendar=calendar
    )
    # Fetch students who registered for this course in this calendar
    registrations = RegisteredCourse.objects.filter(
        course_id=course_id,
        academic_calendar=calendar
    ).select_related('student')

    if request.method == 'POST':
        for reg in registrations:
            prefix = f"reg_{reg.id}_"
            ca1 = request.POST.get(prefix + 'ca1', 0) or 0
            ca2 = request.POST.get(prefix + 'ca2', 0) or 0
            ca3 = request.POST.get(prefix + 'ca3', 0) or 0
            exam = request.POST.get(prefix + 'exam', 0) or 0

            result, created = StudentResult.objects.get_or_create(registered_course=reg) #get_or_create() returns a tuple
            result.ca1 = ca1
            result.ca2 = ca2
            result.ca3 = ca3
            result.exam = exam
            result.updated_by = request.user
            result.save()

        messages.success(request, "✅ Results saved successfully.")
        return redirect(request.path)  # reload page to clear form inputs

    context = {
        'assigned_course': assigned_course,
        'calendar': calendar,
        'registrations': registrations,
    }
    return render(request, 'staff/partials/result_upload.html', context)





def upload_result_dashboard (request):
    academic_calendar = AcademicCalendar.objects.filter(is_current=True).first()
    assigned_course = AssignCourse.objects.filter(
        academic_staff=request.user.academicstaff,
        academic_calendar = academic_calendar
        ).select_related('course')
    context={
        'assigned_course': assigned_course,
        'academic_calendar': academic_calendar
    }
    return render(request, 'staff/partials/upload_result_dashboard.html',context)



def assigned_course(request):
    assigned_course = AssignCourse.objects.filter(academic_staff=request.user.academicstaff)
    context={'assigned_course': assigned_course}
    return render(request, 'staff/partials/assigned_course.html', context)

def academicstaff_home (request):
    return render(request, 'staff/academicstaff_home.html')





