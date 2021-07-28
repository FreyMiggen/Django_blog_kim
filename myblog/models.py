from django.db import models
from django.db.models.deletion import SET_DEFAULT, SET_NULL
from django.db.models.fields import DateTimeField
from django.db.models.fields.related import ForeignKey, ManyToManyField
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.


class Post(models.Model):
    title=models.CharField(max_length=120,null=True)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    time=models.DateTimeField(auto_now_add=True,null=True)
    author=models.ForeignKey(User,on_delete=SET_NULL,null=True)
    content=RichTextField(blank=True,null=True)
    likes=models.ManyToManyField(User,related_name='blog_likes')
    
    def __str__(self):
        return self.title
    def total_likes(self):
        return self.likes.count()

    def delete(self,*args,**kwargs): # override predefined delete method to delete an file from storage directory instead of just an instance
        self.header_image.delete()
        super().delete(*args,**kwargs)


        


