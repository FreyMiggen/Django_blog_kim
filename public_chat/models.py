from django.db import models
from django.conf import settings

# Create your models here.

class PublicChatRoom(models.Model):
    title = models.CharField(max_length=200,unique=True,blank=False)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL,blank=True,help_text="users who are connected to the chatroom")

    def __str__(self):
        return self.title
    
    def connect_user(self,user):
        is_connected=False
        if user not in self.users.all():
            self.users.add(user)
            self.save()
            is_connected=True
        else:
            is_connected=True

        return is_connected
    

    def disconnect_user(self,user):
        is_disconnected=False
        if user in self.users.all():
            self.users.remove(user)
            self.save()
            is_disconnected=True
        else:
            is_disconnected=True

        return is_disconnected

    @property
    def group_name(self):
        # Return the group name that socket get subcribed to and get sent message as they are generated
        return f"PublicChatRoom-{self.id}"

class PublicChatRoomMessageManager(models.Manager):
    def by_room(self,room):
        qs=PublicChatRoomMessage.objects.filter(room=room).order_by('timestamp')
        return qs

class PublicChatRoomMessage(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    room = models.ForeignKey(PublicChatRoom,on_delete=models.CASCADE)
    timestamp=models.DateTimeField(auto_now_add=True)
    content=models.TextField(unique=False,blank=False)
    objects = PublicChatRoomMessageManager()


