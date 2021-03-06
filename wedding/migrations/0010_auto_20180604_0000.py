# Generated by Django 2.0.2 on 2018-06-04 00:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wedding', '0009_auto_20180603_2355'),
    ]

    operations = [
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('relation', models.CharField(max_length=120)),
            ],
            options={
                'verbose_name_plural': 'People',
            },
        ),
        migrations.RemoveField(
            model_name='person',
            name='user',
        ),
        migrations.AlterField(
            model_name='quote',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wedding.Local'),
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
