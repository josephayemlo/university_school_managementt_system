from django.db import models
from django_countries.fields import CountryField
from datetime import date






class Faculty(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=100)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='departments')

    class Meta:
        unique_together = ('name', 'faculty')  # name must be unique within a faculty

    def __str__(self):
        return f"{self.name} ({self.faculty.name})"

        
class CourseOfStudy(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='courses_of_study')
    
    duration_years = models.PositiveIntegerField(default=4)
    # this unique together just allows us to have same department name under different faculty bu
    # same dptm mame cannot exist in same faculty
    class Meta:
        unique_together = ('name', 'department')

    def __str__(self):
        return f"{self.name} ({self.department.name})"


class PersonalStatement(models.Model):
    personal_statement = models.FileField(upload_to='personal_statement/')
    title = models.CharField(max_length=50)


    def __str__(self):
        return self.title



class Course(models.Model):
    COURSE_CATEGORIES = (
        ('core', 'Core'),
        ('elective', 'Elective'),
        ('general', 'General'),  # Optional
    )

    code = models.CharField(max_length=10)
    title = models.CharField(max_length=100)
    unit = models.PositiveIntegerField()
    semester = models.CharField(max_length=10, choices=[('first', 'First'), ('second', 'Second')])
    level = models.PositiveIntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    category = models.CharField(max_length=10, choices=COURSE_CATEGORIES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class RegisteredCourse(models.Model):
    student = models.ForeignKey('studentportal.Student', on_delete=models.CASCADE)
    course = models.ForeignKey('core.Course', on_delete=models.CASCADE)
    session = models.CharField(max_length=20)
    semester = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    approved_by = models.ForeignKey('accounts.CustomUser', on_delete=models.SET_NULL, null=True, blank=True)
    approved_at = models.DateTimeField(null=True, blank=True)
    is_repeat_course = models.BooleanField(default=False)
    is_locked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student} - {self.course.code}"

class StudentResult(models.Model):
    student = models.ForeignKey('studentportal.Student', on_delete=models.CASCADE)
    registered_course = models.OneToOneField('RegisteredCourse', on_delete=models.CASCADE)

    session = models.CharField(max_length=20)
    semester = models.CharField(max_length=10)

    ca1 = models.DecimalField(max_digits=5, decimal_places=2, default=0)  # e.g. 10.0
    ca2 = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    exam = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    grade_point = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    remark = models.TextField(null=True, blank=True)
    is_released = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    updated_by = models.ForeignKey('accounts.CustomUser', on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def total(self):
        return self.ca1 + self.ca2 + self.exam

    def grade_letter(self):
        total = self.total
        if total >= 70:
            return 'A'
        elif total >= 60:
            return 'B'
        elif total >= 50:
            return 'C'
        elif total >= 45:
            return 'D'
        elif total >= 40:
            return 'E'
        else:
            return 'F'



class SemesterResult(models.Model):
    student = models.ForeignKey('studentportal.Student', on_delete=models.CASCADE)
    session = models.CharField(max_length=20)
    semester = models.CharField(max_length=10)


















class UndergraduateApplication(models.Model):
    GENDER = [("M", "Male"), ("F", "Female")]
   
    # Bio Data
     # Bio Data
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=15, choices=GENDER)
    dob = models.DateField(null=True, blank=True)
    email = models.EmailField(max_length=255)
    phone_number = models.CharField(max_length=255)
    address_1 = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state_province = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    country = CountryField()
    
        # course details
    course_of_study = models.ForeignKey(CourseOfStudy, on_delete=models.DO_NOTHING)




class ScholarshipApplication(models.Model):
    GENDER = [("M", "Male"), ("F", "Female")]
    DAY_OF_BIRTH = [
        ("1", "1"), ("2", "2"), ("3", "3"),("4", "4"),("5", "5"),("6", "6"),("7", "7"),("8", "8"),("9", "9"),("10", "10"),
        ("11", "11"),("12", "12"),("13", "13"),("14", "14"),("15", "15"),("16", "16"),("17", "17"),("18", "18"),("19", "19"),("20", "20"),
        ("21", "21"),("22", "22"),("23", "23"),("24", "24"),("25", "25"),("26", "26"),("27", "27"),("28", "28"),("29", "29"),("30", "30"),("31", "31"),]
    MONTH_OF_BIRTH = [
        ("Ja", "January"), ("Fe", "Febraury"),("Ma", "March"),("Ap", "April"),("My", "May"),("Jn", "June"),
        ("Jy", "July"),("Ag", "August"),("Sp", "September"),("Oc", "October"),("Nv", "November"),("Dc", "December"),]
    YEAR_OF_BIRTH = [
        ("23", "2023"), ("22", "2022"),("21", "2021"),("20", "2020"),("19", "2019"),("18", "2018"),("17", "2017"),
        ("16", "2016"),("15", "2015"),("14", "2014"),("13", "2013"),("12", "2012"),("11", "2011"),("10", "2010"),]
    
  
     # Bio Data
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=15, choices=GENDER)
    day_of_birth = models.CharField(max_length=15, choices=DAY_OF_BIRTH)
    month_of_birth = models.CharField(max_length=15, choices=MONTH_OF_BIRTH)
    year_of_birth = models.CharField(max_length=15, choices=YEAR_OF_BIRTH)
    email = models.EmailField(max_length=255)
    phone_number = models.CharField(max_length=255)
    address_1 = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state_province = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    country = CountryField( )
    course_applied = models.ForeignKey(CourseOfStudy, on_delete=models.DO_NOTHING)
    # scholarship 
    about_yourself = models.CharField(max_length=255)
    career_plans = models.CharField(max_length=255)
    role_model = models.CharField(max_length=255)
    reasons_for_course_school_choice = models.CharField(max_length=255)
    why_you_deserve_scholarship = models.CharField(max_length=255)
    your_greatest_achievement = models.CharField(max_length=255)
    your_strenths = models.CharField(max_length=255)
    your_weaknesses = models.CharField(max_length=255)
    challenge_faced_overcomed = models.CharField(max_length=255)
    your_leadership_experience = models.CharField(max_length=255)
    activities_involved_in_school_community = models.CharField(max_length=255)
    additional_statement = models.CharField(max_length=255)








    
    
    