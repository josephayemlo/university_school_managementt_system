from django.db import models

from django.conf import settings

# Create your models here.





# students
class Student(models.Model):
    LEVEL_CHOICES = [
    (100, "100 Level"),
    (200, "200 Level"),
    (300, "300 Level"),
    (400, "400 Level"),
    (500, "500 Level"),
    (600, "600 Level"),
    ]
    admin = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='student')
    matric_no = models.CharField(max_length=20, unique=True, blank=False, null=False)
    course_of_study = models.ForeignKey('core.CourseOfStudy', on_delete=models.SET_NULL, null=True)
    level = models.PositiveIntegerField(choices=LEVEL_CHOICES)
    date_of_admission = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.admin.email)



