# Generated by Django 2.0.2 on 2018-05-18 22:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wedding', '0007_auto_20180518_2243'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]