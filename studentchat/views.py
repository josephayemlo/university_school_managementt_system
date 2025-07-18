from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model
from core.models import Student
from .models import PrivateMessage, ChatRoom, GroupMessage, ChatRoom, ChatRoomMembership
User = get_user_model()
from django.http import HttpResponseForbidden
from .forms import ChatRoomForm
from django.contrib import messages


# Chat Dashboard
def chat_dashboard(request):
    return render(request, 'studentchat/student/chat_dashboard.html')

# Chat Management
def chat_management(request):
    return render(request, 'studentchat/chat_management.html')

# permmission
def is_admin(user):
    return user.is_authenticated and user.is_superuser

@login_required
@user_passes_test(is_admin)
def create_group_chat_room(request):
    if request.method == 'POST':
        form = ChatRoomForm(request.POST)
        if form.is_valid():
            chat_room = form.save(commit=False)
            chat_room.created_by = request.user
            chat_room.save()
            messages.success(request,'Group Created Successfully you can create another or exit')
            return redirect(request.path)  # Change to your room listing view
    else:
        form = ChatRoomForm()

    return render(request, 'studentchat/create_group_chat.html', { 'form': form })

# Manage Group Chat
def manage_group_chat(request):
    groupchat = ChatRoom.objects.all()
    return render(request, 'studentchat/manage_group_chat.html', { 'groupchat': groupchat })


# edit
def edit_group_chat(request, group_chat_id):
    group_chat = get_object_or_404(ChatRoom, id=group_chat_id)
    if request.method == 'POST':
        form = ChatRoomForm(request.POST, instance=group_chat)
        if form.is_valid():
            form.save()
            messages.success(request, 'Group Chat Updated Sucessfully')
            return redirect(request.path)
    else:
        form = ChatRoomForm(instance=group_chat)
    context = {
        "form": form,
        "group_chat": group_chat
    }
    return render(request, 'studentchat/edit_group_chat.html', context)


@login_required
def private_chat_view(request, user_id):
    other_user = get_object_or_404(User, id=user_id)
    # getting previous messages
    messages = PrivateMessage.objects.filter(
        sender__in=[request.user, other_user],
        receiver__in=[request.user, other_user]
    ).order_by('timestamp')
    context ={
        'other_user': other_user,
        'messages': messages,
        }
    return render(request, 'studentchat/student/private_chat.html', context)







def student_chat_list(request):
    student = request.user.student
    current_user = request.user

    student_list = Student.objects.filter(
        course_of_study=student.course_of_study,
        level = student.level
    ).exclude(admin=current_user) #the current user cant be in the list... i.e user should not chat with self

    return render(request, 'studentchat/student/student_list.html', {'student_list': student_list})


@login_required
def group_chat_view(request, room_id):
    room = get_object_or_404(ChatRoom, id=room_id)

    # Access restriction: only students of this dept + level
    student = request.user.student
    if room.department != student.course_of_study.department or room.level != student.level:
        return HttpResponseForbidden("You are not allowed in this room.")

    messages = GroupMessage.objects.filter(room=room).order_by("timestamp")

    return render(request, "studentchat/student/group_chat.html", {
        "room": room,
        "messages": messages,
    })



@login_required
def available_group_rooms(request):
    student = request.user.student  

    rooms = ChatRoom.objects.filter(
        department=student.course_of_study.department,
        level=student.level
    )

    joined_room_ids = ChatRoomMembership.objects.filter(
        user=request.user
    ).values_list('room_id', flat=True)

    return render(request, 'studentchat/student/available_rooms.html', {
        'rooms': rooms,
        'joined_room_ids': joined_room_ids
    })

@login_required
def join_group_room(request, room_id):
    student = request.user.student
    room = get_object_or_404(ChatRoom, id=room_id)

    # Validate dept + level
    if room.department != student.course_of_study.department or room.level != student.level:
        return HttpResponseForbidden("You can't join this room.")

    # Add to membership if not already joined
    ChatRoomMembership.objects.get_or_create(user=request.user, room=room)

    return redirect('group_chat', room_id=room.id)