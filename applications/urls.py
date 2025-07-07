from django.urls import path
from . import views

urlpatterns = [

    path("study/apply/", views.apply, name='apply'),
    path("study/apply/undergradute/", views.apply_Undergraduate, name='apply_undergraduate'),
    path("study/apply/undergradute/process", views.apply_Undergraduate_Process, name='apply_undergraduate_process'),
    path("study/apply/postgraduate", views.apply_Postgraduate, name='apply_postgraduate'),
    path("study/apply/undergraduate/application/form", views.undergraduate_Application_Form_View, name='undergraduate_application_form'),
    path('apply/scholarship/', views.scholarship_Application_Form_View, name='scholarship_application_form'),
    path('personal_statement/download/', views.personal_statement_download, name='personal_statement_download'),
    path("success/", views.success, name='success'),


]