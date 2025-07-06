from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from core.models import (
    AcademicCalendar,DepartmentSchoolFee, 
    StudentSchoolFee, SchoolFeeItem, FailedPayment
)
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from django.urls import reverse
import requests
from django.http import HttpResponseRedirect
import uuid
from django.utils import timezone
from core.models.utils import generate_reference





def pay_school_fee(request, invoice_id):
    student = request.user.student
    invoice = get_object_or_404(StudentSchoolFee, id=invoice_id, student=student)

    if invoice.is_paid:
        messages.info(request, "This invoice has already been paid.")
        return redirect('student_invoice_details', invoice_id=invoice.id)
    

    #Regenerate reference ONLY if last one failed
    if invoice.status == 'failed':
        invoice.reference = generate_reference()
        invoice.status = 'pending'
        invoice.last_payment_attempt = timezone.now()
        invoice.save()

    # prepares paystack payment request
    headers = {
        "Authorization": f"Bearer {settings.PAYSTACK_SECRET_KEY}",
        "Content-Type": "application/json",
    }

    callback_url = request.build_absolute_uri(reverse('payment_callback'))

    payment_data = {
        "email": student.admin.email,
        "amount": int(invoice.total_amount * 100), #paystack uses kobo
        "reference": invoice.reference,
        "callback_url": callback_url,
    }
    # sending the data to paystack
    response = requests.post(settings.PAYSTACK_INITIALIZE_URL, json=payment_data, headers=headers)
    res_data = response.json()

    if res_data.get('status') is True:
        return HttpResponseRedirect(res_data['data']['authorization_url'])
    else:
        invoice.status = 'failed'     
        invoice.save()
         # save failed payment reference for audit
        failedpayment = FailedPayment.objects.create(
            student = invoice.student,
            department = invoice.department,
            level = invoice.level,
            academic_calendar  = invoice.academic_calendar,
            total_amount  = invoice.total_amount,
            reference  = invoice.reference
        )
        failedpayment.save()
        print('Payment failed, saved copy')
        messages.error(request, "Payment initialization failed.")
        return redirect('student_invoice_details', invoice_id=invoice.id)



def payment_callback(request):
    reference = request.GET.get('reference')
    if not reference:
        messages.error(request, "No reference provided.")
        return redirect('manage_student_invoice')

    headers = {
        "Authorization": f"Bearer {settings.PAYSTACK_SECRET_KEY}",
    }

    verify_url = f"{settings.PAYSTACK_VERIFY_URL}{reference}"
    response = requests.get(verify_url, headers=headers)
    res_data = response.json()
    # print(res_data) use for debug

    if res_data['status'] and res_data['data']['status'] == 'success':
        invoice = StudentSchoolFee.objects.filter(reference=reference).first()
        if invoice and not invoice.is_paid:
            invoice.is_paid = True
            invoice.status = 'success'
            invoice.save()
            messages.success(request, " Payment successful.")
        else:
            messages.info(request, "Invoice already marked as paid.")
    else:
        invoice = StudentSchoolFee.objects.filter(reference=reference).first()
        if invoice:
            invoice.status = 'failed'
            invoice.save()
        messages.error(request, " Payment verification failed.")

    return redirect('manage_student_invoice')



def student_invoice_details(request, invoice_id):
    student = request.user.student

    # Make sure the invoice belongs to the logged-in student
    invoice = get_object_or_404(StudentSchoolFee, id=invoice_id, student=student)

    context = {
        'invoice': invoice,
        'student': student,
        'items': invoice.items.all()  # List of SchoolFeeItem objects
    }


    return render(request, 'studentportal/partials/schoolfeespayment/student_invoice_details.html', context)



def manage_student_invoice(request):
    student = request.user.student

    # Get current session (not semester)
    current_calendar = AcademicCalendar.objects.filter(is_current=True).first()
    if not current_calendar:
        messages.warning(request, "No current academic session set.")
        return redirect('student_portal')  # or wherever you want to send them

    current_session = current_calendar.session

    # Fetch all invoices for current session regardless of semester
    invoices = StudentSchoolFee.objects.filter(
        student=student,
        academic_calendar__session=current_session
    ).select_related('academic_calendar').prefetch_related('items').order_by('academic_calendar__semester')

    context = {
        'student': student,
        'current_session': current_session,
        'invoices': invoices
    }

    return render(request, 'studentportal/partials/schoolfeespayment/manage_student_invoice.html', context)

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



def generate_student_invoice(request):
    if request.method == 'POST':
        print('request is post')
        student = request.user.student
        department_fee_id = request.POST.get('department_fee_id')

        department_fee = get_object_or_404(DepartmentSchoolFee, id=department_fee_id)

        # Prevent duplicate invoice for same student, level, and academic calendar
        existing_invoice = StudentSchoolFee.objects.filter(
            student=student,
            department=student.course_of_study.department,
            level=student.level,
            academic_calendar=department_fee.academic_calendar
        ).first()
        if existing_invoice:
            messages.warning(request, "You have already generated school fees for this semester.")
            print('Existing Invoice')
            return render(request,'studentportal/partials/error.html')

        # Create the student invoice
        student_invoice = StudentSchoolFee.objects.create(
            student=student,
            department=student.course_of_study.department,
            level=student.level,
            academic_calendar=department_fee.academic_calendar,
            total_amount=department_fee.total_amount
        )

        # Copy each department fee item into student's personalized items
        for item in department_fee.items.all():
            SchoolFeeItem.objects.create(
                student_fee=student_invoice,
                name=item.title,
                amount=item.amount
            )

        messages.success(request, "School fee generated successfully.")
        print('New invoice created sucessfully')
        return render(request,'management/partials/success.html')
    return redirect('student_portal')