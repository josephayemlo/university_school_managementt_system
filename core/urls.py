from . import views
from django.urls import path, re_path
from django.views.static import serve 
from django.conf import settings
urlpatterns = [
    path("", views.home, name='home'),
    path("study/apply/", views.apply, name='apply'),
    path("study/apply/undergradute/", views.apply_Undergraduate, name='apply_undergraduate'),
    path("study/apply/undergradute/process", views.apply_Undergraduate_Process, name='apply_undergraduate_process'),
    path("study/apply/postgraduate", views.apply_Postgraduate, name='apply_postgraduate'),
    path("study/apply/undergraduate/application/form", views.undergraduate_Application_Form_View, name='undergraduate_application_form'),
    path('success/', views.success, name='success'),
    path('apply/scholarship/', views.scholarship_Application_Form_View, name='scholarship_application_form'),


    # download link test
    path('personal_statement/download/', views.personal_statement_download, name='personal_statement_download'),
    path('add-faculty/', views.add_faculty, name='add_faculty'),
    path('add-department/', views.add_department, name='add_department'),
    path('add-course-of-study/', views.add_course_of_study, name='add_course_of_study'),

]