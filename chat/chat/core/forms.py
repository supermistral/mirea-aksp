from django import forms


class ChatRoomInviteForm(forms.Form):
    username = forms.CharField(min_length=3, max_length=20)
    invite_code = forms.CharField(max_length=40)


class ChatRoomCreateForm(forms.Form):
    username = forms.CharField(min_length=3, max_length=20)
