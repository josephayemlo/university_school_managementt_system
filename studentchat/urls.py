from django.urls import path
from . import views

urlpatterns = [
    path('privatechat/<int:user_id>/', views.private_chat_view, name='private_chat'),
    path('chat_dashboard/', views.chat_dashboard, name='chat_dashboard'),
    path('student_list/', views.student_list, name='student_list'),
    path('group-rooms/', views.available_group_rooms, name='available_group_rooms'),
    path('join-group-room/<int:room_id>/', views.join_group_room, name='join_group_room'),
    path('group-chat/<int:room_id>/', views.group_chat_view, name='group_chat'),

    # Admin
    path('chat_management/', views.chat_management, name='admin_chat_management'),
    path('create_group_chat_room/', views.create_group_chat_room, name='admin_create_group_chat_room'),
    path('manage_group_chat/', views.manage_group_chat, name='admin_manage_group_chat'),
    path('edit_group_chat/<int:group_chat_id>/', views.edit_group_chat, name='admin_edit_group_chat'),





]
