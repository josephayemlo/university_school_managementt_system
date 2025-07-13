from django.shortcuts import render
from core.models import AcademicStaff, NonAcademicStaff, Student
from django.db.models import Count
# Create your views here.

def management_home (request):
    total_academicstaff = AcademicStaff.objects.all().count()
    total_nonacademicstaff = NonAcademicStaff.objects.all().count()
    total_students = Student.objects.all().count()



    male_count = Student.objects.filter(admin__gender='M').count()
    female_count = Student.objects.filter(admin__gender='F').count()
    total = male_count + female_count or 1  # avoid division by zero

    male_percent = round((male_count / total) * 100)
    female_percent = round((female_count / total) * 100)
    # Department summary
    data = (
        Student.objects.values("course_of_study__department__name")
        .annotate(total=Count("id")) #this just get all student id in a department and count them
        .order_by("course_of_study__department__name")
    )
    department_name = [item["course_of_study__department__name"] for item in data]
    student_count = [item["total"] for item in data]

    
    context = {
        'total_academicstaff': total_academicstaff,
        'total_nonacademicstaff': total_nonacademicstaff,
        'total_students': total_students,
        'male_percent': male_percent,
        'female_percent': female_percent,
        'male_count': male_count,
        'female_count': female_count,
        'department_name': department_name,
        'student_count': student_count,
    }
    return render(request, 'management/management_home.html', context)
