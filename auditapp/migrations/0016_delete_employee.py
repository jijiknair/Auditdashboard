# Generated by Django 5.1 on 2024-09-19 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auditapp', '0015_employeenew_delete_chatmessage'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Employee',
        ),
    ]