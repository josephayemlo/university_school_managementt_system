from django.urls import path
from . import views

urlpatterns = [
    path('privatechat/<int:user_id>/', views.private_chat_view, name='private_chat'),
    path('chat_dashboard/', views.chat_dashboard, name='chat_dashboard'),
    path('student_list/', views.student_list, name='student_list'),
    path('chat_management/', views.chat_management, name='chat_management'),
    path('create_group_chat_room/', views.create_group_chat_room, name='create_group_chat_room'),
    path('group-rooms/', views.available_group_rooms, name='available_group_rooms'),
    path('join-group-room/<int:room_id>/', views.join_group_room, name='join_group_room'),
    path('group-chat/<int:room_id>/', views.group_chat_view, name='group_chat'),




]
