# Generated by Django 5.1 on 2024-08-27 10:12

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("overseapp", "0002_delete_office"),
    ]

    operations = [
        migrations.CreateModel(
            name="Office",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("location", models.CharField(max_length=255)),
                ("rent_per_hour", models.DecimalField(decimal_places=2, max_digits=10)),
                ("image", models.ImageField(upload_to="office_images/")),
            ],
        ),
    ]
