from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    user=request.user.username
    return render(request,'public_chat/index.html',{'user':user})

def room(request,room_name):
    user=request.user
    if PublicChatRoom.objects.filter(title=room_name):
        chat_room=PublicChatRoom.objects.get(title=room_name)
        messages=PublicChatRoomMessage.objects.by_room(chat_room)
        chat_room.connect_user(user)
        

    else:
        chat_room=PublicChatRoom.objects.create(title=room_name)
        chat_room.users.add(user)
        
        messages=PublicChatRoomMessage.objects.by_room(chat_room)

    return render(request,'public_chat/room.html',{'user':user,'chat_room':chat_room,'messages':messages})



