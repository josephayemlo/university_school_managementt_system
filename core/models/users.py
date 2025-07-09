from django.db import models
from django.conf import settings
from django.contrib.auth.models import UserManager, AbstractUser
from django.db import models
from django.contrib.auth.hashers import make_password
from django_countries.fields import CountryField
from core.models.enums import LevelChoices, AcademicStaffPosition, AcademicStaffRole, NonAcademicStaffRole


# models
class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = CustomUser(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        assert extra_fields["is_staff"]
        assert extra_fields["is_superuser"]
        return self._create_user(email, password, **extra_fields)



# Tha main user having three categories. This will be attched to another 
# model with a one-to-one relatioship 
# The customuser will be thr admin having ability to create new users
class CustomUser(AbstractUser):
    USER_TYPE = ((1, "Management"), (2, "AcademicStaff"),(3, "NonAcademicStaff"), (4, "Student"),  (5, "AspirantStudent"))
    GENDER = [("M", "Male"), ("F", "Female")]

    username = None  # Removed username, using email instead
    email = models.EmailField(unique=True)
    user_type = models.CharField(default=1, choices=USER_TYPE, max_length=1)
    gender = models.CharField(max_length=1, choices=GENDER)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.last_name + ", " + self.first_name


# aspirant students
class AspirantStudent(models.Model):
    EMERGENCY_RELATIONSHIP = [("B", "Brother"), ("S", "Sister"),("F", "Father"),("M", "Mother"), ("O", "Other"),]
    ADMISSION_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('admitted', 'Admitted'),
        ('rejected', 'Rejected'),
    ]
    admin = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='aspirant')
    course_applied = models.ForeignKey('core.CourseOfStudy', on_delete=models.SET_NULL, null=True, blank=True)
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
    level = models.CharField(max_length=3, choices=LevelChoices.choices)
    date_of_admission = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.admin.email)


# Lecturers
class AcademicStaff(models.Model):
    admin = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='academicstaff')
    position = models.CharField(max_length=20, choices=AcademicStaffPosition.choices, default=AcademicStaffPosition.GRADUATE_ASSISTANT)
    role = models.CharField(max_length=20, choices=AcademicStaffRole.choices, default=AcademicStaffRole.STAFF)
    department = models.ForeignKey('core.Department', on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.admin.first_name} ({self.get_position_display()}, {self.get_role_display()})"
    # get is used because of enums we want to get the readable field rather than PROF we get Professor



# Secretary, security.. etc
class NonAcademicStaff(models.Model):
    admin = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='nonacademicstaff')
    role = models.CharField(max_length=20, choices=NonAcademicStaffRole.choices, default=NonAcademicStaffRole.STAFF)

    def __str__(self):
        return str(self.admin.email)


