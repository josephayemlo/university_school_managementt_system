from django import forms
from django.forms import TextInput, EmailInput, Textarea
from .models import UndergraduateApplication, ScholarshipApplication
from django.core.exceptions import ValidationError
from .models import Faculty, Department, CourseOfStudy

class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ['name']

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'faculty']


class CourseOfStudyForm(forms.ModelForm):
    class Meta:
        model = CourseOfStudy
        fields = ['name', 'department', 'duration_years']


# Scholarship Form
class ScholarshipApplicationForm(forms.ModelForm):
    class Meta:
        model = ScholarshipApplication
        fields = '__all__'
        widgets = {
            'first_name': TextInput( attrs={
                'class':'Input',
                'style': 'max-width: 1000px;',
                'placeholder': 'Enter First name'
            }),
             'last_name': TextInput( attrs={
                'class':'Input',
                'style': 'max-width: 1000px;',
                'placeholder': 'Enter Last name'
            }),
             
               'email': EmailInput( attrs={
                'class':'Input',
                'style': 'max-width: 1000px;',
                'placeholder': 'Enter Email'
            }),
               'phone_number': TextInput( attrs={
                'class':'Input',
                'style': 'max-width: 1000px;',
                'placeholder': 'Enter Phone Number'
            }),
              'address_1': TextInput( attrs={
                'class':'InputWide',
                'style': 'max-width: 1000px;',
                'placeholder': 'Enter  Street Address '
            }),
              'address_2': TextInput( attrs={
                'class':'InputWide',
                'style': 'max-width: 1000px;',
                'placeholder': 'Enter Address 2'
            }),
               'city': TextInput( attrs={
                'class':'Input',
                'style': 'max-width: 1000px;',
                'placeholder': 'Enter City'
            }),
               'state_province': TextInput( attrs={
                'class':'Input',
                'style': 'max-width: 1000px;',
                'placeholder': 'Enter State/Province'
            }),
               'postal_code': TextInput( attrs={
                'class':'Input',
                'style': 'max-width: 1000px;',
                'placeholder': 'Enter Postal/Zip Code'
            }),     
               'about_yourself': Textarea( attrs={
                'class':'Textarea',
                'style': 'max-width: 1000px;',
            }),   
                'career_plans': Textarea( attrs={
                'class':'Textarea',
                'style': 'max-width: 1000px;',
            }),   
                'role_model': Textarea( attrs={
                'class':'Textarea',
                'style': 'max-width: 1000px;',
            }),   
                'reasons_for_course_school_choice': Textarea( attrs={
                'class':'Textarea',
                'style': 'max-width: 1000px;',
            }),   
                'why_you_deserve_scholarship': Textarea( attrs={
                'class':'Textarea',
                'style': 'max-width: 1000px;',
            }),   
                'your_greatest_achievement': Textarea( attrs={
                'class':'Textarea',
                'style': 'max-width: 1000px;',
            }),   
                'your_strenths': Textarea( attrs={
                'class':'Textarea',
                'style': 'max-width: 1000px;',
            }),   
                'your_weaknesses': Textarea( attrs={
                'class':'Textarea',
                'style': 'max-width: 1000px;',
            }),   
                'challenge_faced_overcomed': Textarea( attrs={
                'class':'Textarea',
                'style': 'max-width: 1000px;',
            }),   
                'your_leadership_experience': Textarea( attrs={
                'class':'Textarea',
                'style': 'max-width: 1000px;',
            }),   
                'activities_involved_in_school_community': Textarea( attrs={
                'class':'Textarea',
                'style': 'max-width: 1000px;',
            }),   
                'additional_statement': Textarea( attrs={
                'class':'Textarea',
                'style': 'max-width: 1000px;',
            }), 

        # label
        }
        labels = {
            'first_name': ('First Name'),
            'last_name': ('Last Name'),         
            'gender': ('Gender'),
            'day_of_birth': ('Day'),
            'month_of_birth': ('Month'),
            'year_of_birth': ('Year'),
            'address_1': ('Street Address'),
            'address_2': ('Street Address Line 2'),
            'city': ('City'),
            'state_province': ('State/Province'),
            'postal_code': ('Postal/Zip code'),
            'country': ('Country'),
         }
# UG Form
class UndergraduateApplicationForm(forms.ModelForm):
    email=forms.EmailField( )
    emergency_email=forms.EmailField()
    referee_email=forms.EmailField()

    class Meta:
        model = UndergraduateApplication
        fields = '__all__'
        widgets = {
            'first_name': TextInput( attrs={
                'class':'Input',
                'style': 'max-width: 1000px;',
                'placeholder': 'Enter First name'
            }),
             'last_name': TextInput( attrs={
                'class':'Input',
                'style': 'max-width: 1000px;',
                'placeholder': 'Enter Last name'
            }),
             
               'email': EmailInput( attrs={
                'class':'Input',
                'style': 'max-width: 1000px;',
                'placeholder': 'Enter Email'
            }),
               'phone_number': TextInput( attrs={
                'class':'Input',
                'style': 'max-width: 1000px;',
                'placeholder': 'Enter Phone Number'
            }),
              'address_1': TextInput( attrs={
                'class':'InputWide',
                'style': 'max-width: 1000px;',
                'placeholder': 'Enter  Street Address '
            }),
              'address_2': TextInput( attrs={
                'class':'InputWide',
                'style': 'max-width: 1000px;',
                'placeholder': 'Enter Address 2'
            }),
               'city': TextInput( attrs={
                'class':'Input',
                'style': 'max-width: 1000px;',
                'placeholder': 'Enter City'
            }),
               'state_province': TextInput( attrs={
                'class':'Input',
                'style': 'max-width: 1000px;',
                'placeholder': 'Enter State/Province'
            }),
               'postal_code': TextInput( attrs={
                'class':'Input',
                'style': 'max-width: 1000px;',
                'placeholder': 'Enter Postal/Zip Code'
            }),     

             # school data
                'school_name': TextInput( attrs={
                'class':'Input',
                'style': 'max-width: 1000px;',
                'placeholder': 'Enter School name'
            }),
                'school_address_1': TextInput( attrs={
                'class':'Input',
                'style': 'max-width: 1000px;',
                'placeholder': 'Enter School Address'
            }),
                'school_address_2': TextInput( attrs={
                'class':'Input',
                'style': 'max-width: 1000px;',
                'placeholder': 'Enter School Address 2'
            }),
                'school_city': TextInput( attrs={
                'class':'Input',
                'style': 'max-width: 1000px;',
                'placeholder': 'Enter City'
            }),
                'school_state_province': TextInput( attrs={
                'class':'Input',
                'style': 'max-width: 1000px;',
                'placeholder': 'Enter State/Province'
            }),
                'school_postal_code': TextInput( attrs={
                'class':'Input',
                'style': 'max-width: 1000px;',
                'placeholder': 'Enter Postal/Zip code'
            }),
              'school_year_graduated': TextInput( attrs={
                'class':'Input',
                'style': 'max-width: 1000px;',
                'placeholder': 'e.g 2020'
            }),
            'emergency_first_name': TextInput( attrs={
                'class':'Input',
                'style': 'max-width: 1000px;',
                'placeholder': 'Enter First Name'
            }),
                'emergency_last_name': TextInput( attrs={
                'class':'Input',
                'style': 'max-width: 1000px;',
                'placeholder': 'Enter Last Name'
            }),
                'emergency_email': TextInput( attrs={
                'class':'Input',
                'style': 'max-width: 1000px;',
                'placeholder': 'Enter email'
            }),
                'emergency_phone_number': TextInput( attrs={
                'class':'Input',
                'style': 'max-width: 1000px;',
                'placeholder': '+12333333'
            }),
                'emergency_address_1': TextInput( attrs={
                'class':'Input',
                'style': 'max-width: 1000px;',
                'placeholder': 'enter address'
            }),
              'emergency_address_2': TextInput( attrs={
                'class':'Input',
                'style': 'max-width: 1000px;',
                'placeholder': 'enter address 2'
            }),
            'emergency_city': TextInput( attrs={
                'class':'Input',
                'style': 'max-width: 1000px;',
                'placeholder': 'enter city'
            }),
              'emergency_postal_code': TextInput( attrs={
                'class':'Input',
                'style': 'max-width: 1000px;',
                'placeholder': 'enter postal/zip code'
            }),

          
               # 
                'referee_first_name': TextInput( attrs={
                'class':'Input',
                'style': 'max-width: 1000px;',
                'placeholder': 'Enter First Name'
            }),
                'referee_last_name': TextInput( attrs={
                'class':'Input',
                'style': 'max-width: 1000px;',
                'placeholder': 'Enter Last Name'
            }),
                'referee_email': TextInput( attrs={
                'class':'Input',
                'style': 'max-width: 1000px;',
                'placeholder': 'Enter email'
            }),
                'referee_phone_number': TextInput( attrs={
                'class':'Input',
                'style': 'max-width: 1000px;',
                'placeholder': '+12333333'
            }),
                'referee_address_1': TextInput( attrs={
                'class':'Input',
                'style': 'max-width: 1000px;',
                'placeholder': 'enter address'
            }),
                'referee_address_2': TextInput( attrs={
                'class':'Input',
                'style': 'max-width: 1000px;',
                'placeholder': 'enter address 2'
            }),
                'referee_city': TextInput( attrs={
                'class':'Input',
                'style': 'max-width: 1000px;',
                'placeholder': 'enter city'
            }),
                'referee_postal_code': TextInput( attrs={
                'class':'Input',
                'style': 'max-width: 1000px;',
                'placeholder': 'enter postal/zip code'
            }),
                'referee_state_province': TextInput( attrs={
                'class':'Input',
                'style': 'max-width: 1000px;',
                'placeholder': 'enter state/province'
            }),
           
        }
        labels = {
            'first_name': ('First Name'),
            'last_name': ('Last Name'),         
            'gender': ('Gender'),
            'day_of_birth': ('Day1'),
            'month_of_birth': ('Month'),
            'year_of_birth': ('Year'),
            'address_1': ('Street Address'),
            'address_2': ('Street Address Line 2'),
            'city': ('City'),
            'state_province': ('State/Province'),
            'postal_code': ('Postal/Zip code'),
            'country': ('Country'),


            'school_name': ('School Name'),
            'school_address_1': ('Address'),
            'school_address_2': ('Address 2'),
            'school_city': ('City'),
            'school_state_province': ('State/Province'),
            'school_postal_code': ('Postal/Zip code'),
            'school_year_graduated': ('Year of graduation'),

            'emergency_first_name': ('First Name'),
            'emergency_last_name': ('Last Name'),       
            'emergency_email': ('Email'),     
            'emergency_phone_number': ('Phone Number'),   
            'emergency_address_1': ('Street Address'),      
            'emergency_address_2': ('Street Address Line 2'),  
            'emergency_city': ('City'),     
            'emergency_postal_code': ('Postal/Zip Code'),   

            'referee_first_name': ('First Name'),
            'referee_last_name': ('Last Name'),       
            'referee_email': ('Email'),     
            'referee_phone_number': ('Phone Number'),   
            'referee_address_1': ('Street Address'),      
            'referee_address_2': ('Street Address Line 2'),  
            'referee_city': ('City'),     
            'referee_postal_code': ('Postal/Zip Code'),   
            'referee_state_province': ('State/Province'), 
            
        }


