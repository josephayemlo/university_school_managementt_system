from django import forms
from core.models import Course

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
