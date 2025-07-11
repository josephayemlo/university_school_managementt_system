from django.conf import settings
from django.db import models
from core.models.enums import LevelChoices

User = settings.AUTH_USER_MODEL   # keeps it flexible if you swap auth models

class ChatRoom(models.Model):
    name        = models.CharField(max_length=100)
    department  = models.ForeignKey('core.Department', on_delete=models.CASCADE) 
    level = models.CharField(max_length=3, choices=LevelChoices.choices)
    created_by  = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_rooms')
    created_at  = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('department', 'level', 'name')   # optional but avoids dupes

    def __str__(self):
        return f"{self.department}-{self.level}: {self.name}"


class ChatRoomMembership(models.Model):
    user       = models.ForeignKey(User, on_delete=models.CASCADE, related_name='room_memberships')
    room       = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name='memberships')
    joined_at  = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'room')


class GroupMessage(models.Model):
    room      = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name='messages')
    sender    = models.ForeignKey(User, on_delete=models.CASCADE)
    body      = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['timestamp']


class PrivateMessage(models.Model):
    sender    = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_private')
    receiver  = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_private')
    body      = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['timestamp']
        indexes  = [models.Index(fields=['sender', 'receiver'])]  # speeds up lookups
