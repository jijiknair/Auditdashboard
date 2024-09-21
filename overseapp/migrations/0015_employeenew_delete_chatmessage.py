# Generated by Django 5.1 on 2024-09-18 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('overseapp', '0014_analyticsdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employeenew',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('job_position', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='ChatMessage',
        ),
    ]
