from django import forms
from core.models import AspirantStudent


class AdmissionStatusForm(forms.ModelForm):
    class Meta:
        model = AspirantStudent
        fields = ['admission_status']
