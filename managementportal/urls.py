from . import views
from django.urls import path
from .customviews.student_result_views import (
    result_registeredcourse_students, result_select_department, 
    result_department_course,semester_result,semester_results_list, compute_semester_result_individual, 
    compute_all_semester_results, compute_all_semester_results_dashboard, compute_by_department,
    release_by_department, release_all_results, release_all_results_dashboard, unrelease_all_results

)
from .customviews.aspirant_views import add_aspirant, manage_aspirant, edit_aspirant, delete_aspirant
from .customviews.student_views import add_student, manage_student, edit_student, delete_student
from .customviews.academic_staff_views import (
    add_academicstaff, manage_academicstaff, 
    edit_academicstaff, delete_academicstaff,assign_course, 
    manage_assigned_course, edit_assigned_course, delete_assigned_course
    )
from .customviews.nonacademic_staff_views import add_nonacademicstaff, manage_nonacademicstaff, edit_nonacademicstaff, delete_nonacademicstaff
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
    edit_academic_calender,
    add_aspirant_academic_calender, manage_aspirant_academic_calender,
    edit_aspirant_academic_calender
)
from .customviews.navigation_views import (
    department_and_faculty, academic_course,
    session_and_academic_calender, result_and_assessment,
    student_management, student_school_fees_management, 
    academic_staff, nonacademic_staff, aspirant_management
)
from .customviews.student_school_fees_views import (
    add_department_school_fees, 
    add_item_to_department_school_fee,
    manage_department_school_fees,
    department_fee_item
)

from .customviews.addmission_views import addmissions, addmissions_courses, addmissions_applicants, change_addmission_status

# URLs
urlpatterns = [
    
    # ManagementPortal Home URL
    path("management/home", views.management_home, name='management_home'),

    # Student School Fees
    path("add_department_school_fees/", add_department_school_fees, name='admin_add_department_school_fees'),
    path("add_item_to_department_school_fee/", add_item_to_department_school_fee, name='admin_add_item_to_department_school_fee'),
    path("manage_department_school_fees/", manage_department_school_fees, name='admin_manage_department_school_fees'),
    path('department_fee_item/<int:department_fee_id>/', department_fee_item, name='admin_department_fee_item'),


    # Result
    path("result_select_department", result_select_department, name='admin_result_select_department'),
    path('department/<int:department_id>/courses/', result_department_course, name='admin_result_department_course'),
    path('course/<int:course_id>/students/', result_registeredcourse_students, name='admin_result_registeredcourse_students'),
    path("semester_result", semester_result, name='admin_semester_result'),
    path('admin/semester-results/', semester_results_list, name='admin_semester_results_list'),
    path('admin/compute-semester-result/<int:result_id>/', compute_semester_result_individual, name='admin_compute_semester_result_individual'),
    path('admin/compute-all-results/', compute_all_semester_results, name='admin_compute_all_semester_results'),
    path('admin/compute-all-results/dashboard', compute_all_semester_results_dashboard, name='admin_compute_all_semester_results_dashboard'),
    path('admin/compute-by-department/', compute_by_department, name='admin_compute_by_department'),
    path('admin/release-by-department/', release_by_department, name='admin_release_by_department'),
    path('admin/release-all/result', release_all_results, name='admin_release_all_results'),
    path('admin/unrelease-all/result', unrelease_all_results, name='admin_unrelease_all_results'),

    path('admin/release-all/dashboard', release_all_results_dashboard, name='admin_release_all_results_dashboard'),







    # aspirant URL
    path("aspirant/add", add_aspirant, name='admin_add_aspirant'),
    path("aspirant/list", manage_aspirant, name='admin_manage_aspirant'),
    path("aspirant/edit/<int:aspirant_id>/", edit_aspirant, name='admin_edit_aspirant'),
    path("aspirant/delete/<int:aspirant_id>", delete_aspirant, name='admin_delete_aspirant'),

    # student URL
    path("student/add", add_student, name='admin_add_student'),
    path("student/list", manage_student, name='admin_manage_student'),
    path("student/edit/<int:student_id>/", edit_student, name='admin_edit_student'),
    path("student/delete/<int:student_id>", delete_student, name='admin_delete_student'),

    # academic staff URL
    path("academicstaff/add", add_academicstaff, name='admin_add_academicstaff'),
    path("academicstaff/list", manage_academicstaff, name='admin_manage_academicstaff'),
    path("academicstaff/edit/<int:academicstaff_id>/",edit_academicstaff, name='admin_edit_academicstaff'),
    
    path("academicstaff/delete/<int:academicstaff_id>", delete_academicstaff, name='admin_delete_academicstaff'),
    path("assign_course", assign_course, name='admin_assign_course'),
    path('manage_assigned_course/', manage_assigned_course, name='admin_manage_assigned_course'),
    path('assigned_course/edit/<int:assigned_course_id>/', edit_assigned_course, name='admin_edit_assigned_course'),
    path('assigned_course/delete/<int:assigned_course_id>/', delete_assigned_course, name='admin_delete_assigned_course'),

    # nonacademic staff URL
    path("nonacademicstaff/add", add_nonacademicstaff, name='admin_add_nonacademicstaff'),
    path("nonacademicstaff/list", manage_nonacademicstaff, name='admin_manage_nonacademicstaff'),
    path("nonacademicstaff/edit/<int:nonacademicstaff_id>",edit_nonacademicstaff, name='admin_edit_nonacademicstaff'),
    path("nonacademicstaff/delete/<int:nonacademicstaff_id>", delete_nonacademicstaff, name='admin_delete_nonacademicstaff'),

    # faculty URL
    path('faculty/add/', add_faculty, name='admin_add_faculty'),
    path('faculty/manage/', manage_faculty, name='admin_manage_faculty'),
    path('faculty/edit/<int:faculty_id>/', edit_faculty, name='admin_edit_faculty'),
    path('faculty/delete/<int:faculty_id>/', delete_faculty, name='admin_delete_faculty'),

    # department URL
    path('department/add/', add_department, name='admin_add_department'),
    path('department/manage/', manage_department, name='admin_manage_department'),
    path('department/edit/<int:department_id>/', edit_department, name='admin_edit_department'),
    path('department/delete/<int:department_id>/', delete_department, name='admin_delete_department'),

    # course_of_study URL
    path('course_of_study/add/', add_course_of_study, name='admin_add_course_of_study'),
    path('course_of_study/manage/', manage_course_of_study, name='admin_manage_course_of_study'),
    path('course_of_study/edit/<int:course_id>/', edit_course_of_study, name='admin_edit_course_of_study'),
    path('course_of_study/delete/<int:course_id>/', delete_course_of_study, name='admin_delete_course_of_study'),

    # course URL
    path('course/add/', add_course, name='admin_add_course'),
    path('course/manage/', manage_course, name='admin_manage_course'),
    path('course/edit/<int:course_id>/', edit_course, name='admin_edit_course'),
    path('course/delete/<int:course_id>/', delete_course, name='admin_delete_course'),

    # level_course URL
    path('level_course/assign/', assign_level_course, name='admin_assign_level_course'),
    path('level_course/manage/', manage_level_course, name='admin_manage_level_course'),
    path('level_course/edit/<int:course_id>/', edit_level_course, name='admin_edit_level_course'),
    path('level_course/delete/<int:course_id>/', delete_level_course, name='admin_delete_level_course'),

    # academic calendar URL
    path('academic_calendar/add/', add_academic_calender, name='admin_add_academic_calender'),
    path('academic_calendar/manage/', manage_academic_calender, name='admin_manage_academic_calender'),
    path('academic_calendar/edit/<int:academic_calender_id>/', edit_academic_calender, name='admin_edit_academic_calender'),

    # aspirant academic calendar URL
    path('aspirant_academic_calendar/add/', add_aspirant_academic_calender, name='admin_add_aspirant_academic_calender'),
    path('aspirant_academic_calendar/manage/', manage_aspirant_academic_calender, name='admin_manage_aspirant_academic_calender'),
    path('aspirant_academic_calendar/edit/<int:aspirant_academic_calender_id>/', edit_aspirant_academic_calender, name='admin_edit_aspirant_academic_calender'),

    # navigation URL
    path('student_management/', student_management, name='admin_student_management'),
    path('result_and_assessment/', result_and_assessment, name='admin_result_and_assessment'),
    path('session_and_academic_calender/', session_and_academic_calender, name='admin_session_and_academic_calender'),
    path('academic_course/', academic_course, name='admin_academic_course'),
    path('department_and_faculty/', department_and_faculty, name='admin_department_and_faculty'),
    path("student_school_fees_management/", student_school_fees_management, name='admin_student_school_fees_management'),
    path('academic_staff/', academic_staff, name='admin_academic_staff'),
    path('nonacademic_staff/', nonacademic_staff, name='admin_nonacademic_staff'),
    path('aspirant_management/', aspirant_management, name='admin_aspirant_management'),

    # Addmission
    path("addmissions/",addmissions, name='admin_addmissions'),
    path('addmissions/<int:session_id>/courses/', addmissions_courses, name='admin_addmissions_courses'),
    path('addmissions/<int:session_id>/courses/<int:course_id>/applicants/', addmissions_applicants, name='admin_addmissions_applicants'),
    path('addmissions/<int:aspirant_id>/', change_addmission_status, name='admin_change_addmission_status'),



]