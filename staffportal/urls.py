from . import views
from django.urls import path
from staffportal.customviews import nonacademicstaff_home, addmissions, addmissions_courses, addmissions_applicants, change_addmission_status

urlpatterns = [

    # academicstaff
    path("academicstaff/home", views.academicstaff_home, name='academicstaff_home'),
    path("assigned_course", views.assigned_course, name='acdstaff_assigned_course'),
    path("upload_result_dashboard", views.upload_result_dashboard, name='acdstaff_upload_result_dashboard'),
    path("result_upload/<int:course_id>/", views.result_upload, name='acdstaff_result_upload'),

    # Nonacademicstaff
    path("nonacademicstaff/home",nonacademicstaff_home, name='nonacademicstaff_home'),
    path("addmissions/",addmissions, name='nonacdstaff_addmissions'),
    path('admissions/<int:session_id>/courses/', addmissions_courses, name='nonacdstaff_addmissions_courses'),
    path('admissions/<int:session_id>/courses/<int:course_id>/applicants/', addmissions_applicants, name='nonacdstaff_addmissions_applicants'),
    path('admissions/<int:aspirant_id>/', change_addmission_status, name='nonacdstaff_change_addmission_status'),







]