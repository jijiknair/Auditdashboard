# Generated by Django 5.1 on 2024-08-27 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('overseapp', '0004_officenew_delete_office'),
    ]

    operations = [
        migrations.AlterField(
            model_name='officenew',
            name='owner',
            field=models.CharField(max_length=255),
        ),
    ]