from . import views
from django.urls import path

urlpatterns = [
    path("student/home", views.student_home, name='student_home'),
    path("aspirant_student/home", views.aspirant_student_home, name='aspirant_student_home'),
    path("student/edit/aspirant_student>",views.edit_aspirant_student, name='edit_aspirant_student'),
]