from . import views #issue
from django.urls import path, reverse_lazy
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path ('', views.login_page, name='login_page'),
    path("login_user/", views.login_user, name='login_user'),
    path("logout/", views.logout_user, name='logout_user'),

    
    # password reset
   path('reset_password/', auth_views.PasswordResetView.as_view(
        template_name='accounts/registration/password_reset_form.html',
        success_url=reverse_lazy('password_reset_done')
    ), name='reset_password'),

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(
        template_name='accounts/registration/password_reset_done.html'
    ), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='accounts/registration/password_reset_confirm.html',
        success_url=reverse_lazy('password_reset_complete')
    ), name='password_reset_confirm'),

    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='accounts/registration/password_reset_complete.html'
    ), name='password_reset_complete'),
 
]
