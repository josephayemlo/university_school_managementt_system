from . import views
from django.urls import path

urlpatterns = [
    path("management/home", views.management_home, name='management_home'),

    # create view
    path("nonacademicstaff/add", views.add_nonacademicstaff, name='add_nonacademicstaff'),
    path("academicstaff/add", views.add_academicstaff, name='add_academicstaff'),
    path("student/add", views.add_student, name='add_student'),
    path("aspirant_student/add", views.add_aspirant_student, name='add_aspirant_student'),


    # list view
    path("student/list", views.student_list, name='student_list'),
    path("aspirant_student/list", views.aspirant_student_list, name='aspirant_student_list'),

    path("academicstaff/list", views.academicstaff_list, name='academicstaff_list'),
    path("nonacademicstaff/list", views.nonacademicstaff_list, name='nonacademicstaff_list'),

    # update view
    path("academicstaff/edit/<int:academicstaff_id>",views.edit_academicstaff, name='edit_academicstaff'),
    path("nonacademicstaff/edit/<int:nonacademicstaff_id>",views.edit_nonacademicstaff, name='edit_nonacademicstaff'),
    path("student/edit/<int:student_id>",views.edit_student, name='edit_student'),

    # delete view
    path("academicstaff/delete/<int:academicstaff_id>", views.delete_academicstaff, name='delete_academicstaff'),
    path("nonacademicstaff/delete/<int:nonacademicstaff_id>", views.delete_nonacademicstaff, name='delete_nonacademicstaff'),
    path("student/delete/<int:student_id>", views.delete_student, name='delete_student'),


]