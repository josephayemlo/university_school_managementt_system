from . import views
from django.urls import path

urlpatterns = [
    path("academicstaff/home", views.academicstaff_home, name='academicstaff_home'),
    path("nonacademicstaff/home", views.nonacademicstaff_home, name='nonacademicstaff_home'),
    path("assigned_course", views.assigned_course, name='assigned_course'),
    path("upload_result_dashboard", views.upload_result_dashboard, name='upload_result_dashboard'),
    path("result_upload/<int:course_id>/", views.result_upload, name='result_upload'),




]