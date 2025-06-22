from django.db import models

from django.conf import settings
from core.models import CourseOfStudy
from django_countries.fields import CountryField

# Create your models here.

# aspirant students
class AspirantStudent(models.Model):
    EMERGENCY_RELATIONSHIP = [("B", "Brother"), ("S", "Sister"),("F", "Father"),("M", "Mother"), ("O", "Other"),]
    ADMISSION_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('admitted', 'Admitted'),
        ('rejected', 'Rejected'),
    ]
    admin = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course_applied = models.ForeignKey(CourseOfStudy, on_delete=models.SET_NULL, null=True, blank=True)
    phone_number = models.CharField(max_length=255)
    address_1 = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state_province = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    country = CountryField()
    admission_status = models.CharField(max_length=10, choices=ADMISSION_STATUS_CHOICES, default='pending')
   


        # Educational Information
    school_name = models.CharField(max_length=255)
    school_address_1 = models.CharField(max_length=255)
    school_address_2 = models.CharField(max_length=255)
    school_city = models.CharField(max_length=255)
    school_state_province = models.CharField(max_length=255)
    school_postal_code = models.CharField(max_length=255)
    school_year_graduated = models.CharField(max_length=255)

    # Emergency contact details
    emergency_first_name = models.CharField(max_length=255)
    emergency_last_name = models.CharField(max_length=255)
    emergency_email = models.EmailField(max_length=255)
    emergency_phone_number = models.CharField(max_length=255)
    emergency_address_1 = models.CharField(max_length=255)
    emergency_address_2 = models.CharField(max_length=255)
    emergency_city = models.CharField(max_length=255)
    emergency_postal_code = models.CharField(max_length=255)
    emergency_country = CountryField( )
    emergency_relationship = models.CharField(max_length=15, choices=EMERGENCY_RELATIONSHIP)

    # Refreee
    referee_first_name = models.CharField(max_length=255)
    referee_last_name = models.CharField(max_length=255)
    referee_email = models.EmailField(max_length=255)
    referee_phone_number = models.CharField(max_length=255)
    referee_address_1 = models.CharField(max_length=255)
    referee_address_2 = models.CharField(max_length=255)
    referee_city = models.CharField(max_length=255)
    referee_postal_code = models.CharField(max_length=255)
    referee_state_province = models.CharField(max_length=255)
    referee_country = CountryField()

    def __str__(self):
        return str(self.admin.email)

  





# students
class Student(models.Model):
    admin = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='student')
    matric_no = models.CharField(max_length=20, unique=True, blank=False, null=False)
    course_of_study = models.ForeignKey('core.CourseOfStudy', on_delete=models.SET_NULL, null=True)
    level = models.CharField(max_length=10)
    date_of_admission = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.admin.email)



