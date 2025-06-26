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
    path('add_course/', views.add_course, name='add_course'),
    path('student_management/', views.student_management, name='student_management'),
    path('course_and_academic/', views.course_and_academic, name='course_and_academic'),
    path('session_and_calender/', views.session_and_calender, name='session_and_calender'),
    path('department_and_faculty/', views.department_and_faculty, name='department_and_faculty'),
    path('result_and_assessment/', views.result_and_assessment, name='result_and_assessment'),
    path('manage_course/', views.manage_course, name='manage_course'),
    path('edit_course/<int:course_id>', views.edit_course, name='edit_course'),
    path('delete_course/<int:course_id>/', views.delete_course, name='delete_course'),



]