from django.shortcuts import redirect, render

from .models import ChatRoom
from .forms import ChatRoomInviteForm, ChatRoomCreateForm


def index(request):
    if request.method == 'GET':
        form_invite = ChatRoomInviteForm(request.GET)
        form_create = ChatRoomCreateForm()

        if form_invite.is_valid():
            username = form_invite.cleaned_data['username']
            invite_code = form_invite.cleaned_data['invite_code']

            print(invite_code)

            chatroom = ChatRoom.objects.get_by_invite_code(invite_code)

            return redirect(
                'chatroom',
                invite_code=invite_code,
                username=username
            )
    else:
        form_invite = ChatRoomInviteForm()

        if request.method == 'POST':
            form_create = ChatRoomCreateForm(request.POST)

            if form_create.is_valid():
                username = form_create.cleaned_data['username']
                chatroom = ChatRoom.objects.create()

                return redirect(
                    'chatroom',
                    invite_code=chatroom.invite_code,
                    username=username
                )

    context = {
        'form_invite': form_invite,
        'form_create': form_create
    }

    return render(request, 'core/index.html', context)


def chatroom(request, invite_code, username):
    chatroom = ChatRoom.objects.get_by_invite_code(invite_code)
    context = {
        'invite_code': invite_code,
        'chatroom': chatroom,
        'username': username
    }
    return render(request, 'core/chatroom.html', context)
