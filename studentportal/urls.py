from . import views
from django.urls import path

urlpatterns = [
    path("student/home", views.student_home, name='student_home'),
    path("aspirant_student/home", views.aspirant_student_home, name='aspirant_student_home'),
    path("student/edit/aspirant_student/",views.edit_aspirant_student, name='edit_aspirant_student'),
    path("student/course_registration", views.course_registration, name='course_registration'),
    path("student/available_course", views.student_available_course, name='student_available_course'),
    path("student/register_course", views.register_courses, name='register_courses'),
    path("student/student_portal", views.student_portal, name='student_portal'),


]