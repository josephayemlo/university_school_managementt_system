from . import views
from django.urls import path

# URLs
urlpatterns = [
    path("", views.home, name='home'),
    
    # Student URLs
    path("student/home", views.student_home, name='student_home'),

    #Aspirant URL
    path("aspirant_student/home", views.aspirant_student_home, name='aspirant_student_home'),


]