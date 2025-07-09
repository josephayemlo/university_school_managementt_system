from django import forms
from django_countries.fields import CountryField
from django import forms
from .models import (
    Student, 
    AspirantStudent, 
    AcademicStaff, 
    NonAcademicStaff, 
    CustomUser, 
    CourseOfStudy,
    StudentResult,
    DepartmentSchoolFee,
    DepartmentFeeItem,
    AssignCourse

)



class AssignCourseForm(forms.ModelForm):
    class Meta:
        model = AssignCourse
        fields = {'course', 'academic_staff', 'academic_calendar'}


class DepartmentSchoolFeeForm(forms.ModelForm):
    class Meta:
        model = DepartmentSchoolFee
        fields = {'department', 'academic_calendar','level'}
    

class DepartmentFeeItemForm(forms.ModelForm):
    class Meta:
        model = DepartmentFeeItem
        fields = '__all__'
# Forms
class FormSettings(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FormSettings, self).__init__(*args, **kwargs)
        # Here make some changes such as:
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'


class CustomUserForm(FormSettings):
    email = forms.EmailField(required=True)
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')])
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    address = forms.CharField(widget=forms.Textarea)
    password = forms.CharField(widget=forms.PasswordInput)
    widget = {
        'password': forms.PasswordInput(),
    }

    def __init__(self, *args, **kwargs):
        super(CustomUserForm, self).__init__(*args, **kwargs)

        if kwargs.get('instance'):
            instance = kwargs.get('instance').admin.__dict__
            self.fields['password'].required = False
            for field in CustomUserForm.Meta.fields:
                self.fields[field].initial = instance.get(field)
            if self.instance.pk is not None:
                self.fields['password'].widget.attrs['placeholder'] = "Fill this only if you wish to update password"

    def clean_email(self, *args, **kwargs):
        formEmail = self.cleaned_data['email'].lower()
        if self.instance.pk is None:  # Insert
            if CustomUser.objects.filter(email=formEmail).exists():
                raise forms.ValidationError(
                    "The given email is already registered")
        else:  # Update
            dbEmail = self.Meta.model.objects.get(
                id=self.instance.pk).admin.email.lower()
            if dbEmail != formEmail:  # There has been changes
                if CustomUser.objects.filter(email=formEmail).exists():
                    raise forms.ValidationError("The given email is already registered")

        return formEmail

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'gender',  'password', 'address' ]




class NonAcademicStaffForm(CustomUserForm):
    def __init__(self, *args, **kwargs):
        super(NonAcademicStaffForm, self).__init__(*args, **kwargs)

    class Meta(CustomUserForm.Meta):
        model = NonAcademicStaff
        fields = CustomUserForm.Meta.fields 
            

class AcademicStaffForm(CustomUserForm):
    
    class Meta(CustomUserForm.Meta):
        model = AcademicStaff
        fields = CustomUserForm.Meta.fields + [ 'position', 'role','department']
            


class StudentForm(CustomUserForm):
    class Meta(CustomUserForm.Meta):
        model = Student
        fields = CustomUserForm.Meta.fields + [
            'matric_no',
            'course_of_study',
            'level',
        ]
          
# class StudentForm(CustomUserForm):
#     class Meta(CustomUserForm.Meta):
#         model = Student
#         def __init__(self, *args, **kwargs):
#             self.user = kwargs.pop('user', None)
#             super().__init__(*args, **kwargs)
#             if self.user and self.user.user_type =="4": #excluding sesitive data in student edit view for student
#                 fields = CustomUserForm.Meta.fields + [ ]
#             elif self.user and self.user.user_type =="1":
#                 fields = CustomUserForm.Meta.fields + [
#                     'matric_no',
#                     'course_of_study',
#                     'level',
#                 ]
#             else:
#                 fields = CustomUserForm.Meta.fields + [ ]

     

     

class AspirantStudentForm(CustomUserForm):
    course_applied = forms.ModelChoiceField(queryset=CourseOfStudy.objects.all(), label="Course of Study")
    
    # Educational Info
    school_name = forms.CharField(max_length=255)
    school_address_1 = forms.CharField(max_length=255)
    school_address_2 = forms.CharField(max_length=255)
    school_city = forms.CharField(max_length=255)
    school_state_province = forms.CharField(max_length=255)
    school_postal_code = forms.CharField(max_length=255)
    school_year_graduated = forms.CharField(max_length=255)

    # Emergency Info
    emergency_first_name = forms.CharField(max_length=255)
    emergency_last_name = forms.CharField(max_length=255)
    emergency_email = forms.EmailField(max_length=255)
    emergency_phone_number = forms.CharField(max_length=255)
    emergency_address_1 = forms.CharField(max_length=255)
    emergency_address_2 = forms.CharField(max_length=255)
    emergency_city = forms.CharField(max_length=255)
    emergency_postal_code = forms.CharField(max_length=255)
    emergency_country = forms.ChoiceField(
        choices=CountryField().choices,
        widget=forms.Select,
        required=True,
        label="Emergency Contact Country"
    )
    emergency_relationship = forms.ChoiceField(choices=AspirantStudent.EMERGENCY_RELATIONSHIP)

    # Referee Info
    referee_first_name = forms.CharField(max_length=255)
    referee_last_name = forms.CharField(max_length=255)
    referee_email = forms.EmailField(max_length=255)
    referee_phone_number = forms.CharField(max_length=255)
    referee_address_1 = forms.CharField(max_length=255)
    referee_address_2 = forms.CharField(max_length=255)
    referee_city = forms.CharField(max_length=255)
    referee_postal_code = forms.CharField(max_length=255)
    referee_state_province = forms.CharField(max_length=255)
    referee_country = forms.ChoiceField(
        choices=CountryField().choices,
        widget=forms.Select,
        required=True,
        label="Emergency Contact Country"
    )

    class Meta(CustomUserForm.Meta):
        model = AspirantStudent
        fields = CustomUserForm.Meta.fields + [
            'course_applied',
            'phone_number',
            'address_1', 'address_2', 'city', 'state_province', 'postal_code', 'country',
            
            # Educational
            'school_name', 'school_address_1', 'school_address_2', 'school_city',
            'school_state_province', 'school_postal_code', 'school_year_graduated',

            # Emergency
            'emergency_first_name', 'emergency_last_name', 'emergency_email',
            'emergency_phone_number', 'emergency_address_1', 'emergency_address_2',
            'emergency_city', 'emergency_postal_code', 'emergency_country', 'emergency_relationship',

            # Referee
            'referee_first_name', 'referee_last_name', 'referee_email',
            'referee_phone_number', 'referee_address_1', 'referee_address_2',
            'referee_city', 'referee_postal_code', 'referee_state_province', 'referee_country',
        ]

class StudentResultForm(forms.ModelForm):
    class Meta:
        model = StudentResult
        fields = ['registered_course', 'ca1', 'ca2', 'ca3', 'exam', 'grade_point', 'remark', 'is_released']
