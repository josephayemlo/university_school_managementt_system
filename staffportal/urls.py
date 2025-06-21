from . import views
from django.urls import path

urlpatterns = [
    path("academicstaff/home", views.academicstaff_home, name='academicstaff_home'),
    path("nonacademicstaff/home", views.nonacademicstaff_home, name='nonacademicstaff_home'),

]