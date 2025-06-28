from django.shortcuts import render

# Department and Faculty
def department_and_faculty(request):
    return render (request, 'management/partials/navigation/department_and_faculty_links.html')

# Academic Calender 
def session_and_calender(request):
    return render (request, 'management/partials/navigation/session_and_calender_links.html')

# Course and Academics
def course_and_academic(request):
    return render (request, 'management/partials/navigation/course_and_academic_links.html')

# student Management
def student_management(request):
    return render (request, 'management/partials/navigation/student_links.html')

# Result and assessment
def result_and_assessment(request):
    return render (request, 'management/partials/navigation/result_and_assessment_links.html')