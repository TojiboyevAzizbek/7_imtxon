# Generated by Django 5.0.4 on 2024-04-20 05:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_profile_rename_employee_attendance_staff'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]