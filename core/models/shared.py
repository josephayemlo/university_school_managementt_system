from django.db import models
from core.models.enums import LevelChoices, CourseCategoryChoices, SemesterChoices
from django.contrib.auth import get_user_model
User = get_user_model()


# Create your models here.

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

class Course(models.Model):
    code = models.CharField(max_length=10)
    title = models.CharField(max_length=100)
    unit = models.PositiveIntegerField()
    level = models.CharField(max_length=3, choices=LevelChoices.choices)
    semester = models.CharField(max_length=10, choices=SemesterChoices.choices)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    category = models.CharField(max_length=20, choices=CourseCategoryChoices.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# this is used to activate a session only one calalender can take is_current=True
class AspirantAcademicCalendar(models.Model):
    session = models.CharField(max_length=20, unique=True)  # e.g., '2024/2025'
    is_current = models.BooleanField(default=False)

    def __str__(self):
        return self.session

# this is used to activate a session only one calalender can take is_current=True
class AcademicCalendar(models.Model):
    session = models.CharField(max_length=20)  # e.g., '2024/2025'
    semester = models.CharField(max_length=10, choices=SemesterChoices.choices)
    is_current = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.session} - {self.semester}"

class RegisteredCourse(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    academic_calendar = models.ForeignKey('AcademicCalendar', on_delete=models.PROTECT, null=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    approved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    approved_at = models.DateTimeField(null=True, blank=True)
    is_repeat_course = models.BooleanField(default=False)
    is_locked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student} - {self.course.code}"


class LevelCourse(models.Model):
    level = models.CharField(max_length=3, choices=LevelChoices.choices)
    semester = models.CharField(max_length=10, choices=SemesterChoices.choices)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    course_of_study = models.ForeignKey(CourseOfStudy, on_delete=models.CASCADE)
    is_compulsory = models.BooleanField(default=True)

    class Meta:
        unique_together = ('level', 'semester', 'course', 'course_of_study',)
    
    def __str__(self):
        return f"{self.level}L - ({self.semester} Semester) - {self.course_of_study}"


class StudentResult(models.Model):
    semester_result = models.ForeignKey('core.SemesterResult', on_delete=models.CASCADE, null=True, blank=True,  related_name='student_results')
    registered_course = models.OneToOneField('RegisteredCourse', on_delete=models.CASCADE)
    ca1 = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    ca2 = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    ca3 = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    exam = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    remark = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def total_score(self):
        return float(self.ca1 + self.ca2 + self.ca3 + self.exam)

    def get_grade_point(self):
        score = self.total_score()
        if score >= 70:
            return 5.0
        elif score >= 60:
            return 4.0
        elif score >= 50:
            return 3.0
        elif score >= 45:
            return 2.0
        elif score >= 40:
            return 1.0
        return 0.0

    def get_grade_letter(self):
        score = self.total_score()
        if score >= 70:
            return "A"
        elif score >= 60:
            return "B"
        elif score >= 50:
            return "C"
        elif score >= 45:
            return "D"
        elif score >= 40:
            return "E"
        return "F"

    def __str__(self):
        rc = self.registered_course
        return f"{rc.student} - {rc.course} ({rc.academic_calendar})"


class SemesterResult(models.Model):
    student = models.ForeignKey('core.Student', on_delete=models.CASCADE)
    academic_calendar = models.ForeignKey('AcademicCalendar', on_delete=models.PROTECT, null=True, blank=True) #Rm change null to false and remove blank
    total_units_registered = models.PositiveIntegerField(default=0)
    total_units_passed = models.PositiveIntegerField(default=0)
    total_grade_points = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    gpa = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    cgpa = models.DecimalField(max_digits=4, decimal_places=2, default=0) 
    remark = models.CharField(max_length=255, null=True, blank=True)
    is_released = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('student', 'academic_calendar')
    
    def compute_result(self):

        results = StudentResult.objects.filter(
            registered_course__student=self.student,
            registered_course__academic_calendar=self.academic_calendar
        ).select_related('registered_course__course')

        total_units = 0
        total_passed_units = 0
        total_grade_points = 0.0

        for result in results:
            course = result.registered_course.course
            credit_unit = course.unit
            grade_point = result.get_grade_point()

            total_units += credit_unit
            total_grade_points += credit_unit * grade_point

            if grade_point >= 1.0:  # Passed
                total_passed_units += credit_unit

        self.total_units_registered = total_units
        self.total_units_passed = total_passed_units
        self.total_grade_points = round(total_grade_points, 2)
        self.gpa = round((total_grade_points / total_units), 2) if total_units else 0

        # Compute CGPA
        self.cgpa = self.compute_cgpa()

        # Set remark
        self.remark = "PASS" if self.gpa >= 1.0 else "PROBATION" if self.gpa >= 0.5 else "FAIL"

        self.save()

    def compute_cgpa(self):
        past_results = SemesterResult.objects.filter(
            student=self.student,
            is_released=True
        ).exclude(id=self.id)

        total_units = self.total_units_registered
        total_points = float(self.total_grade_points)

        for sr in past_results:
            total_units += sr.total_units_registered
            total_points += float(sr.total_grade_points)

        return round(total_points / total_units, 2) if total_units else 0.0

    
"""
how abut 
"""


class AssignCourse(models.Model):
    course = models.ForeignKey('Course',on_delete=models.CASCADE)
    academic_staff = models.ForeignKey('core.AcademicStaff',on_delete=models.CASCADE)
    academic_calendar = models.ForeignKey('AcademicCalendar', on_delete=models.PROTECT, null=False)
    created_at = models.DateTimeField(auto_now=True)
    class Meta:
        unique_together = ('course', 'academic_staff') #A course should not be assigned twice to one staff t avoid duplicates
    def __str__(self):
        return f"{self.course.title} - {self.academic_staff.admin.first_name}"


