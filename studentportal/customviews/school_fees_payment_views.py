from django.shortcuts import render, get_object_or_404
from django.contrib import messages

def school_fees_dashboard(request):
    student = request.user
    # paid_fees = StudentSchoolFee.objects.filter(student=student, status='paid')
    # pending_fees = StudentSchoolFee.objects.filter(student=student, status='pending')


    return render (request, 'studentportal/partials/schoolfeespayment/school_fees_dashboard.html')