# Generated by Django 4.1 on 2024-11-17 12:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("auditapp", "0030_auditresponsenew_user_auditsummary_user_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="AuditResponsenewfinal",
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
                ("page_number", models.IntegerField()),
                ("ref_no", models.CharField(max_length=10)),
                ("description", models.TextField()),
                (
                    "response",
                    models.CharField(
                        choices=[
                            ("Met", "Met"),
                            ("Partially Met", "Partially Met"),
                            ("Not Met", "Not Met"),
                        ],
                        max_length=20,
                    ),
                ),
                ("audit_date", models.DateField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="AuditSummaryfinal",
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
                ("heading", models.CharField(max_length=255)),
                ("met_count", models.IntegerField(default=0)),
                ("partially_met_count", models.IntegerField(default=0)),
                ("not_met_count", models.IntegerField(default=0)),
                ("comments", models.TextField(blank=True, null=True)),
                (
                    "photo",
                    models.ImageField(blank=True, null=True, upload_to="audit_photos/"),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="FacilityAuditnewfinal",
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
                ("facility_name", models.CharField(max_length=255)),
                ("governate", models.CharField(max_length=100)),
                ("wilayat", models.CharField(max_length=100)),
                ("head_of_institution", models.CharField(max_length=255)),
                ("rationale", models.CharField(max_length=100)),
                ("audit_date", models.DateField()),
                ("lead_auditor", models.CharField(max_length=255)),
                ("auditors", models.TextField()),
                ("areas_covered", models.TextField()),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.RemoveField(
            model_name="auditsummary",
            name="user",
        ),
        migrations.RemoveField(
            model_name="facilityauditnew",
            name="user",
        ),
        migrations.RemoveField(
            model_name="ipcprogram",
            name="user",
        ),
        migrations.DeleteModel(
            name="AuditResponsenew",
        ),
        migrations.DeleteModel(
            name="AuditSummary",
        ),
        migrations.DeleteModel(
            name="FacilityAuditnew",
        ),
    ]