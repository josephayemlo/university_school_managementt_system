from django.db import models

from django.conf import settings
# Create your models here.
# students
class Student(models.Model):
    admin = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='student')
    matric_no = models.CharField(max_length=20, unique=True, blank=False, null=False)
    course_of_study = models.ForeignKey('core.CourseOfStudy', on_delete=models.SET_NULL, null=True)
    level = models.CharField(max_length=10)
    date_of_admission = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.admin.email)
