from core.models import  AspirantStudent

from core.forms import CustomUserForm

class AspirantStudentProfileForm(CustomUserForm):

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
            'session'

           
        ]
