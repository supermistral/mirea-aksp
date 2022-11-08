from __future__ import annotations

from django.db import models

from .tokens import chatroom_token_generator


def generate_invite_code(obj: ChatRoom) -> str:
    return chatroom_token_generator.make_token(obj)


class ChatRoomManager(models.Manager):
    def get_by_invite_code(self, invite_code):
        return self.get(invite_code=invite_code)


class ChatRoom(models.Model):
    invite_code = models.CharField(unique=True, max_length=40, blank=True)

    objects = ChatRoomManager()

    def save(self, *args, **kwargs):
        self.invite_code = generate_invite_code(self)
        return super().save(*args, **kwargs)
