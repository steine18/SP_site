# Generated by Django 2.0.2 on 2018-05-11 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedding', '0004_fund'),
    ]

    operations = [
        migrations.CreateModel(
            name='FunStuff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('category', models.CharField(choices=[('Entertainment', 'Entertainment'), ('Food', 'Food'), ('Outdoors', 'Outdoors')], default='Entertainment', max_length=13)),
                ('link', models.CharField(max_length=400)),
                ('image_source', models.CharField(max_length=120)),
                ('info', models.TextField(blank=True)),
            ],
        ),
    ]
