from django.contrib import admin
from .models import *
from django.contrib.auth import get_user_model
from managementportal.models import *

User = get_user_model()


admin.site.register(User)

admin.site.register(Student)
admin.site.register(AcademicStaff)
# admin.site.register(NonAcademicStaff)
# admin.site.register(UndergraduateApplication)
# admin.site.register(ScholarshipApplication)
# admin.site.register(PersonalStatement)
admin.site.register(AspirantStudent)
admin.site.register(Course)
admin.site.register(StudentResult)
admin.site.register(SemesterResult)
admin.site.register(RegisteredCourse)
admin.site.register(LevelCourse)
admin.site.register(AcademicCalendar)
admin.site.register(StudentSchoolFee)
admin.site.register(SchoolFeeItem)
admin.site.register(DepartmentSchoolFee)
admin.site.register(FailedPayment)
admin.site.register(AssignCourse)





