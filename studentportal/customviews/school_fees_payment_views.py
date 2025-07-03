from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from core.models import AcademicCalendar,DepartmentSchoolFee, StudentSchoolFee, SchoolFeeItem
from core.models import Student, AcademicCalendar
from django.core.exceptions import ObjectDoesNotExist


def school_fees_dashboard(request):
    return render (request, 'studentportal/partials/schoolfeespayment/school_fees_dashboard.html')



def generate_school_fee(request):
    student = request.user.student
    academic_calender = AcademicCalendar.objects.filter(is_current=True).first()
    
    
    school_fees = DepartmentSchoolFee.objects.filter(
    department=student.course_of_study.department,
    level=student.level,
)
   
    print(f"Fees found for level 100: {school_fees.count()}")
    context = {
        'student': student,
        'academic_calender': academic_calender,
        'school_fees': school_fees
    }
    return render(request, 'studentportal/partials/schoolfeespayment/generate_school_fee.html', context)



