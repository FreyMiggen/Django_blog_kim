from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='public-chat-index'),
    path('<str:room_name>/',room,name='public-chat-room')
]