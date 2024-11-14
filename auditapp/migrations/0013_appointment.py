# Generated by Django 5.1 on 2024-09-18 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auditapp', '0012_employee_office'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('office_name', models.CharField(max_length=100)),
                ('office_location', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
        ),
    ]