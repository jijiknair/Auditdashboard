# Generated by Django 4.2.7 on 2024-09-29 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auditapp', '0016_delete_employee'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AnalyticsData',
        ),
        migrations.DeleteModel(
            name='Announcement',
        ),
        migrations.DeleteModel(
            name='Appointment',
        ),
        migrations.DeleteModel(
            name='Employeenew',
        ),
        migrations.RemoveField(
            model_name='resourcerequest',
            name='requested_by',
        ),
        migrations.RemoveField(
            model_name='task',
            name='assigned_to',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Meeting',
        ),
        migrations.DeleteModel(
            name='MeetingRoom',
        ),
        migrations.DeleteModel(
            name='ResourceRequest',
        ),
        migrations.DeleteModel(
            name='Task',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
