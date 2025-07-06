from django.shortcuts import redirect


class ForceAspirantProfileCompletionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        allowed_paths = [
            "/student/edit/aspirant_student",
            "/student/edit/aspirant_student/",
            # you need to get each allowed url with two links using starting slash and trailing slash this else it will loop
            "/accounts/logout/",  
            "accounts/logout",  

        ]
        current_path = request.path

        # Only check for logged-in users
        ASPIRANT_USER_TYPE = 5
        if request.user.is_authenticated and int(request.user.user_type) == ASPIRANT_USER_TYPE:
            try:
                aspirant = request.user.aspirantstudent

                # List of fields required to complete profile
                required_fields = [
                    'school_name',
                    'school_address_1',
                    'school_address_2',
                    'school_city',
                    'school_state_province',
                    'school_postal_code',
                    'school_year_graduated',

                    'emergency_first_name',
                    'emergency_last_name',
                    'emergency_email',
                    'emergency_phone_number',
                    'emergency_address_1',
                    'emergency_address_2',
                    'emergency_city',
                    'emergency_postal_code',
                    'emergency_country',
                    'emergency_relationship',

                    'referee_first_name',
                    'referee_last_name',
                    'referee_email',
                    'referee_phone_number',
                    'referee_address_1',
                    'referee_address_2',
                    'referee_city',
                    'referee_postal_code',
                    'referee_state_province',
                    'referee_country',
                ]
                incomplete = any(
                    not getattr(aspirant, field) for field in required_fields
                )

                if incomplete and current_path not in allowed_paths:
                    print("⚠️ Incomplete profile detected. Redirecting...")
                    return redirect("/student/edit/aspirant_student")
            except AttributeError:
                pass  # User doesn't have an AspirantStudent profile

        return self.get_response(request)
