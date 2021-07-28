# Generated by Django 2.2.13 on 2021-07-27 15:31

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myblog', '0003_delete_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(related_name='blog_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
