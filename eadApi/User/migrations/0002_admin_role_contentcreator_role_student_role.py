# Generated by Django 5.0.7 on 2024-07-13 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='role',
            field=models.CharField(default='admin', max_length=50),
        ),
        migrations.AddField(
            model_name='contentcreator',
            name='role',
            field=models.CharField(default='content_creator', max_length=50),
        ),
        migrations.AddField(
            model_name='student',
            name='role',
            field=models.CharField(default='student', max_length=50),
        ),
    ]
