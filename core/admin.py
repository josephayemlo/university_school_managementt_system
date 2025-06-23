from django.contrib import admin
from accounts.models import AcademicStaff, NonAcademicStaff, Admin
from .models import *
from django.contrib.auth import get_user_model
from studentportal.models import Student, AspirantStudent


User = get_user_model()


admin.site.register(User)

admin.site.register(Student)
admin.site.register(AcademicStaff)
admin.site.register(NonAcademicStaff)
admin.site.register(Admin)
admin.site.register(UndergraduateApplication)
admin.site.register(ScholarshipApplication)
admin.site.register(PersonalStatement)
admin.site.register(AspirantStudent)
admin.site.register(Course)
admin.site.register(StudentResult)
admin.site.register(SemesterResult)
admin.site.register(RegisteredCourse)








