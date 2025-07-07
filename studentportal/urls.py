from . import views
from django.urls import path
from .customviews.school_fees_payment_views import (
    school_fees_dashboard, generate_school_fee,
    manage_student_invoice, generate_student_invoice,
    student_invoice_details, pay_school_fee, payment_callback

)

urlpatterns = [
    
    path("student/course_registration", views.course_registration, name='course_registration'),
    path("student/available_course", views.student_available_course, name='student_available_course'),
    path("student/register_course", views.register_courses, name='register_courses'),
    path("student_portal", views.student_portal, name='student_portal'),
    path("student/registered_courses", views.registered_courses, name='registered_courses'),
    path("student/previous_registered_courses", views.previous_registered_courses, name='previous_registered_courses'),
    path(
    "student/previous_course_registration_details/<int:level>/<str:semester>/",
    views.previous_course_registration_details,
    name="previous_course_registration_details"),
    path("edit_student", views.edit_student, name='edit_student'),

    # School Fees Payment
    path("student/school_fees_dashboard", school_fees_dashboard, name='school_fees_dashboard'),
    path("student/generate_school_fee", generate_school_fee, name='generate_school_fee'),
    path('manage_student_invoice/', manage_student_invoice, name='manage_student_invoice'),
    path('generate-invoice/', generate_student_invoice, name='generate_student_invoice'),
    path('student_invoice_details/<int:invoice_id>/', student_invoice_details, name='student_invoice_details'),
    path('pay/<int:invoice_id>/', pay_school_fee, name='pay_school_fee'),
    path('payment/callback/', payment_callback, name='payment_callback'),


]