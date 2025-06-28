from . import views
from django.urls import path

# URLs
urlpatterns = [
    path("", views.home, name='home'),
    path("study/apply/", views.apply, name='apply'),
    path("study/apply/undergradute/", views.apply_Undergraduate, name='apply_undergraduate'),
    path("study/apply/undergradute/process", views.apply_Undergraduate_Process, name='apply_undergraduate_process'),
    path("study/apply/postgraduate", views.apply_Postgraduate, name='apply_postgraduate'),
    path("study/apply/undergraduate/application/form", views.undergraduate_Application_Form_View, name='undergraduate_application_form'),
    path('apply/scholarship/', views.scholarship_Application_Form_View, name='scholarship_application_form'),
    path('success/', views.success, name='success'),
    path('personal_statement/download/', views.personal_statement_download, name='personal_statement_download'),

    # Student URLs
    path("student/home", views.student_home, name='student_home'),

    #Aspirant URL
    path("aspirant_student/home", views.aspirant_student_home, name='aspirant_student_home'),
    path("aspirant_student/edit/aspirant_student/",views.edit_aspirant_student, name='edit_aspirant_student'),


]