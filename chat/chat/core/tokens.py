from django.contrib.auth.tokens import PasswordResetTokenGenerator


class ChatRoomTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, obj, timestamp):
        return f"{obj.id}{timestamp}"


chatroom_token_generator = ChatRoomTokenGenerator()
