from django import forms
from core.models import Course, Student
from core.forms import CustomUserForm

class CourseRegistrationForm(forms.Form):
    courses = forms.ModelMultipleChoiceField(
        queryset=Course.objects.none(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label="Select your courses"
    )

    def __init__(self, *args, available_courses=None, **kwargs):
        super().__init__(*args, **kwargs)
        if available_courses is not None:
            self.fields['courses'].queryset = available_courses


class StudentProfileForm(CustomUserForm):
    class Meta(CustomUserForm.Meta):
        model = Student
        fields = CustomUserForm.Meta.fields
