from django import forms
from core.models import (
    Faculty,
    LevelCourse,
    AcademicCalendar,
    Department,
    CourseOfStudy,
    Course
)

# Forms
class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ['name']


class LevelCourseForm(forms.ModelForm):
    class Meta:
        model = LevelCourse
        fields = ['level', 'semester', 'course', 'course_of_study', 'is_compulsory']
        widgets = {
            'level': forms.Select(attrs={'class': 'form-control'}),
            'semester': forms.Select(attrs={'class': 'form-control'}),
            'course': forms.Select(attrs={'class': 'form-control'}),
            'course_of_study': forms.Select(attrs={'class': 'form-control'}),
            'is_compulsory': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class AcademicCalenderForm(forms.ModelForm):
    class Meta:
        model = AcademicCalendar
        fields = ['session', 'semester', 'is_current']
        widgets = {
            'sesssion': forms.CharField,
            'semester': forms.Select(attrs={'class': 'form-control'}),
            'is_current': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'faculty']

class CourseOfStudyForm(forms.ModelForm):
    class Meta:
        model = CourseOfStudy
        fields = ['name', 'department', 'duration_years']

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['code', 'title', 'unit','semester', 'level', 'department','category']
