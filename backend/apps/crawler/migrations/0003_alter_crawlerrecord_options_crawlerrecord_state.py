# Generated by Django 4.2 on 2023-09-03 18:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("crawler", "0002_alter_crawlerrecord_companies_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="crawlerrecord",
            options={"ordering": ["-created_at"]},
        ),
        migrations.AddField(
            model_name="crawlerrecord",
            name="state",
            field=models.CharField(
                choices=[
                    ("Complete", "Complete"),
                    ("Failed", "Failed"),
                    ("Process", "Process"),
                ],
                default="Process",
                max_length=20,
            ),
        ),
    ]
