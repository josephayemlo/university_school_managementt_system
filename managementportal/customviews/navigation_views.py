from django.shortcuts import render

# Department and Faculty
def department_and_faculty(request):
    return render (request, 'management/partials/navigation/department_and_faculty_links.html')

# Academic Calender 
def session_and_academic_calender(request):
    return render (request, 'management/partials/navigation/session_and_academic_calender_links.html')

# Course and Academics
def academic_course(request):
    return render (request, 'management/partials/navigation/academic_course_links.html')

# student Management
def student_management(request):
    return render (request, 'management/partials/navigation/student_links.html')

# Result and assessment
def result_and_assessment(request):
    return render (request, 'management/partials/navigation/result_and_assessment_links.html')


# Student School Fees Payment
def student_school_fees_management(request):
    return render (request, 'management/partials/navigation/student_school_fees_links.html')

# Academic Staff
def academic_staff(request):
    return render (request, 'management/partials/navigation/academic_staff_links.html')

# NonAcademic Staff
def nonacademic_staff(request):
    return render (request, 'management/partials/navigation/nonacademic_staff_links.html')