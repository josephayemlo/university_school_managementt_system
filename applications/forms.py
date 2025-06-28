from django import forms
from django.forms import TextInput,DateInput, EmailInput, Textarea
from django_countries.fields import CountryField
from .models import ScholarshipApplication, UndergraduateApplication

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
            'dob': DateInput(attrs={  
                'type': 'date',
                'class': 'Input',
                'style': 'max-width: 1000px;',
                'placeholder': 'Select Date of Birth'
            }),
           
        }
        labels = {
            'first_name': ('First Name'),
            'last_name': ('Last Name'),         
            'gender': ('Gender'),
            'dob': 'Date of Birth', 
            'address_1': ('Street Address'),
            'address_2': ('Street Address Line 2'),
            'city': ('City'),
            'state_province': ('State/Province'),
            'postal_code': ('Postal/Zip code'),
            'country': ('Country'),
             'course_of_study': ('Course Applying'),
            
        }


