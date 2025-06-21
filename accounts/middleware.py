from django.utils.deprecation import MiddlewareMixin
from django.urls import reverse
from django.shortcuts import redirect


class LoginCheckMiddleWare(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        modulename = view_func.__module__
        user = request.user # checking who the user is
        if user.is_authenticated:
            if user.user_type == '1': # checking if it is the managmennt
                if modulename == 'accounts.management_views':
                    return redirect(reverse('management_home'))
                

            elif user.user_type == '2': #  academic staff :-/ ?
                if modulename == 'accounts.student_views' or modulename == 'accounts.management_views':
                    return redirect(reverse('academicstaff_home'))
            
            elif user.user_type == '3': #  nonacademic staff :-/ ?
                if modulename == 'accounts.student_views' or modulename == 'accounts.management_views':
                    return redirect(reverse('nonacademicstaff_home'))
                
            elif user.user_type == '4': # ... or Student ?
                if modulename == 'accounts.management_views' or modulename == 'accounts.academicstaff_views' or modulename == 'accounts.nonacademicstaff_views':
                    return redirect(reverse('student_home'))
            else: # None of the aforementioned ? Please take the user to login page
                return redirect(reverse('login_page'))
        else:
            if request.path == reverse('login_page') or modulename == 'django.contrib.auth.views' or request.path == reverse('login_user'): # If the path is login or has anything to do with authentication, pass
                pass
            else:
                return redirect(reverse('login_page'))
# This file is what causes the automatic redirect to login page no matter the link entered

