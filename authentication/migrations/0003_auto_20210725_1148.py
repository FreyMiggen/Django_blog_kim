# Generated by Django 2.2.13 on 2021-07-25 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20210713_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(related_name='products', to='authentication.Tag'),
        ),
    ]