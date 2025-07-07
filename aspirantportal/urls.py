from django.urls import path
from . import views

urlpatterns = [

    path("aspirant_student/home", views.aspirant_student_home, name='aspirant_student_home'),
    path("edit_aspirant_student/", views.edit_aspirant_student, name='edit_aspirant_student'),
]