# Generated by Django 5.0.7 on 2024-07-14 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='course',
            table='course',
        ),
        migrations.AlterModelTable(
            name='coursecategory',
            table='course_category',
        ),
    ]
