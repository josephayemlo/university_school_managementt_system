from . import views
from django.urls import path
# from staffportal.customviews import nonacademicstaff_home, addmissions, admissions_courses, admissions_applicants, change_addmission_status
from staffportal.customviews import nonacademicstaff_home
urlpatterns = [
    path("academicstaff/home", views.academicstaff_home, name='academicstaff_home'),
    path("assigned_course", views.assigned_course, name='assigned_course'),
    path("upload_result_dashboard", views.upload_result_dashboard, name='upload_result_dashboard'),
    path("result_upload/<int:course_id>/", views.result_upload, name='result_upload'),

    # Nonacademicstaff
    path("nonacademicstaff/home",nonacademicstaff_home, name='nonacademicstaff_home'),
    # path("addmissions/",addmissions, name='addmissions'),
    # path('admissions/<int:session_id>/courses/', admissions_courses, name='admissions_courses'),
    # path('admissions/<int:session_id>/courses/<int:course_id>/applicants/', admissions_applicants, name='admissions_applicants'),
    # path('admissions/<int:aspirant_id>/', change_addmission_status, name='change_addmission_status'),







]