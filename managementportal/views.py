from django.shortcuts import render
from core.models import AcademicStaff, NonAcademicStaff, Student

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

    
    context = {
        'total_academicstaff': total_academicstaff,
        'total_nonacademicstaff': total_nonacademicstaff,
        'total_students': total_students,
        'male_percent': male_percent,
        'female_percent': female_percent,
        'male_count': male_count,
        'female_count': female_count       
    }
    return render(request, 'management/management_home.html', context)
