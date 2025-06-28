from . import views
from django.urls import path

urlpatterns = [
    
    path("student/course_registration", views.course_registration, name='course_registration'),
    path("student/available_course", views.student_available_course, name='student_available_course'),
    path("student/register_course", views.register_courses, name='register_courses'),
    path("student/student_portal", views.student_portal, name='student_portal'),
    path("student/registered_courses", views.registered_courses, name='registered_courses'),
    path("student/previous_registered_courses", views.previous_registered_courses, name='previous_registered_courses'),
    path(
    "student/previous_course_registration_details/<int:level>/<str:semester>/",
    views.previous_course_registration_details,
    name="previous_course_registration_details"),

]