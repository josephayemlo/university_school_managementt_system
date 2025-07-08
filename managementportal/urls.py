from . import views
from django.urls import path
from .customviews.student_result_views import result_registeredcourse_students, result_select_department, result_department_course
from .customviews.aspirant_views import add_aspirant_student, aspirant_student_list
from .customviews.student_views import add_student, manage_student, edit_student, delete_student
from .customviews.academic_staff_views import (
    add_academicstaff, academicstaff_list, 
    edit_academicstaff, delete_academicstaff,assign_course, 
    manage_assigned_course, edit_assigned_course, delete_assigned_course
    )
from .customviews.nonacademic_staff_views import add_nonacademicstaff, nonacademicstaff_list, edit_nonacademicstaff, delete_nonacademicstaff
from .customviews.faculty_views import add_faculty, manage_faculty, edit_faculty, delete_faculty
from .customviews.department_views import add_department, manage_department, edit_department, delete_department
from .customviews.course_views import (
    add_course, edit_course, delete_course, manage_course
)
from .customviews.course_of_study_views import (
    add_course_of_study, edit_course_of_study,
    delete_course_of_study, manage_course_of_study
)
from .customviews.level_course_views import (
    assign_level_course, edit_level_course,
    delete_level_course, manage_level_course
)
from .customviews.academic_calendar_views import (
    add_academic_calender, manage_academic_calender,
    edit_academic_calender
)
from .customviews.navigation_views import (
    department_and_faculty, academic_course,
    session_and_academic_calender, result_and_assessment,
    student_management, student_school_fees_management, academic_staff
)
from .customviews.student_school_fees_views import (
    add_department_school_fees, 
    add_item_to_department_school_fee,
    manage_department_school_fees,
    department_fee_item
)

# URLs
urlpatterns = [
    
    # ManagementPortal Home URL
    path("management/home", views.management_home, name='management_home'),

    # Student School Fees
    path("add_department_school_fees/", add_department_school_fees, name='add_department_school_fees'),
    path("add_item_to_department_school_fee/", add_item_to_department_school_fee, name='add_item_to_department_school_fee'),
    path("manage_department_school_fees/", manage_department_school_fees, name='manage_department_school_fees'),
    path('department_fee_item/<int:department_fee_id>/', department_fee_item, name='department_fee_item'),


    # Result
    path("result_select_department", result_select_department, name='result_select_department'),
    path('department/<int:department_id>/courses/', result_department_course, name='result_department_course'),
    path('course/<int:course_id>/students/', result_registeredcourse_students, name='result_registeredcourse_students'),

    # aspirant URL
    path("aspirant_student/add", add_aspirant_student, name='add_aspirant_student'),
    path("aspirant_student/list", aspirant_student_list, name='aspirant_student_list'),

    # student URL
    path("student/add", add_student, name='add_student'),
    path("student/list", manage_student, name='manage_student'),
    path("student/edit/<int:student_id>/", edit_student, name='edit_student'),
    path("student/delete/<int:student_id>", delete_student, name='delete_student'),

    # academic staff URL
    path("academicstaff/add", add_academicstaff, name='add_academicstaff'),
    path("academicstaff/list", academicstaff_list, name='academicstaff_list'),
    path("academicstaff/edit/<int:academicstaff_id>",edit_academicstaff, name='edit_academicstaff'),
    path("academicstaff/delete/<int:academicstaff_id>", delete_academicstaff, name='delete_academicstaff'),
    path("assign_course", assign_course, name='assign_course'),
    path('manage_assigned_course/', manage_assigned_course, name='manage_assigned_course'),
    path('assigned_course/edit/<int:assigned_course_id>/', edit_assigned_course, name='edit_assigned_course'),
    path('assigned_course/delete/<int:assigned_course_id>/', delete_assigned_course, name='delete_assigned_course'),

    # nonacademic staff URL
    path("nonacademicstaff/add", add_nonacademicstaff, name='add_nonacademicstaff'),
    path("nonacademicstaff/list", nonacademicstaff_list, name='nonacademicstaff_list'),
    path("nonacademicstaff/edit/<int:nonacademicstaff_id>",edit_nonacademicstaff, name='edit_nonacademicstaff'),
    path("nonacademicstaff/delete/<int:nonacademicstaff_id>", delete_nonacademicstaff, name='delete_nonacademicstaff'),

    # faculty URL
    path('faculty/add/', add_faculty, name='add_faculty'),
    path('faculty/manage/', manage_faculty, name='manage_faculty'),
    path('faculty/edit/<int:faculty_id>/', edit_faculty, name='edit_faculty'),
    path('faculty/delete/<int:faculty_id>/', delete_faculty, name='delete_faculty'),


    # department URL
    path('department/add/', add_department, name='add_department'),
    path('department/manage/', manage_department, name='manage_department'),
    path('department/edit/<int:department_id>/', edit_department, name='edit_department'),
    path('department/delete/<int:department_id>/', delete_department, name='delete_department'),

    # course_of_study URL
    path('course_of_study/add/', add_course_of_study, name='add_course_of_study'),
    path('course_of_study/manage/', manage_course_of_study, name='manage_course_of_study'),
    path('course_of_study/edit/<int:course_id>/', edit_course_of_study, name='edit_course_of_study'),
    path('course_of_study/delete/<int:course_id>/', delete_course_of_study, name='delete_course_of_study'),

    # course URL
    path('course/add/', add_course, name='add_course'),
    path('course/manage/', manage_course, name='manage_course'),
    path('course/edit/<int:course_id>/', edit_course, name='edit_course'),
    path('course/delete/<int:course_id>/', delete_course, name='delete_course'),

    # level_course URL
    path('level_course/assign/', assign_level_course, name='assign_level_course'),
    path('level_course/manage/', manage_level_course, name='manage_level_course'),
    path('level_course/edit/<int:course_id>/', edit_level_course, name='edit_level_course'),
    path('level_course/delete/<int:course_id>/', delete_level_course, name='delete_level_course'),

    # academic calendar URL
    path('academic_calendar/add/', add_academic_calender, name='add_academic_calender'),
    path('academic_calendar/manage/', manage_academic_calender, name='manage_academic_calender'),
    path('academic_calendar/edit/<int:academic_calender_id>/', edit_academic_calender, name='edit_academic_calender'),

    # navigation URL
    path('student_management/', student_management, name='student_management'),
    path('result_and_assessment/', result_and_assessment, name='result_and_assessment'),
    path('session_and_academic_calender/', session_and_academic_calender, name='session_and_academic_calender'),
    path('academic_course/', academic_course, name='academic_course'),
    path('department_and_faculty/', department_and_faculty, name='department_and_faculty'),
    path("student_school_fees_management/", student_school_fees_management, name='student_school_fees_management'),
    path('academic_staff/', academic_staff, name='academic_staff'),


]