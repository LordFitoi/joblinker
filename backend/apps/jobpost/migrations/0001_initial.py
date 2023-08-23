# Generated by Django 4.2 on 2023-04-06 23:47

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=100)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Company",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=100)),
                ("logo", models.ImageField(blank=True, null=True, upload_to="")),
                ("website", models.URLField(blank=True, null=True)),
                ("description", models.TextField(blank=True, null=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Location",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=100)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="WebsiteOrigin",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField(blank=True, null=True)),
                ("website", models.URLField(blank=True, null=True)),
                ("json_scrap_origin", models.JSONField(blank=True, null=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="JobPost",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField(blank=True, null=True)),
                ("origin_url", models.URLField(blank=True, null=True)),
                ("application_url", models.URLField(blank=True, null=True)),
                (
                    "job_type",
                    models.CharField(
                        choices=[
                            ("Part Time", "Part Time"),
                            ("Full Time", "Full Time"),
                            ("Contract", "Contract"),
                            ("Internship", "Internship"),
                        ],
                        default="Full Time",
                        max_length=20,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Active", "Active"),
                            ("Inactive", "Inactived"),
                            ("Deleted", "Deleted"),
                            ("Expired", "Expired"),
                        ],
                        default="Active",
                        max_length=20,
                    ),
                ),
                ("currency", models.CharField(default="USD", max_length=10)),
                (
                    "start_salary",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                (
                    "end_salary",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                ("is_remote", models.BooleanField(default=False)),
                ("release_date", models.DateTimeField(blank=True, null=True)),
                (
                    "categories",
                    models.ManyToManyField(blank=True, to="jobpost.category"),
                ),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="jobpost.company",
                    ),
                ),
                (
                    "location",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="jobpost.location",
                    ),
                ),
                (
                    "origin",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="jobpost.websiteorigin",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="company",
            name="location",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="jobpost.location",
            ),
        ),
        migrations.AddField(
            model_name="company",
            name="origin",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="jobpost.websiteorigin"
            ),
        ),
    ]
