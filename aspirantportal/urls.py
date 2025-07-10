from django.urls import path
from . import views

urlpatterns = [

    path("aspirant/home", views.aspirant_home, name='aspirant_home'),
    path("edit_aspirant/", views.edit_aspirant, name='edit_aspirant'),
]