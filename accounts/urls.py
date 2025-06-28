from . import views #issue



from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path ('', views.login_page, name='login_page'),
    path("login_user/", views.login_user, name='login_user'),
    path("logout/", views.logout_user, name='logout_user'),
    # password reset
    path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view()),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view()),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view()),

  
]
