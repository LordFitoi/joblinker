# Generated by Django 4.2 on 2023-04-18 01:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("jobpost", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="jobpost",
            name="application_url",
        ),
        migrations.AlterField(
            model_name="company",
            name="location",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="jobpost.location",
            ),
        ),
        migrations.AlterField(
            model_name="company",
            name="origin",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="jobpost.websiteorigin",
            ),
        ),
        migrations.AlterField(
            model_name="jobpost",
            name="location",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="jobpost.location",
            ),
        ),
        migrations.AlterField(
            model_name="jobpost",
            name="origin",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="jobpost.websiteorigin",
            ),
        ),
        migrations.AlterField(
            model_name="jobpost",
            name="origin_url",
            field=models.URLField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name="jobpost",
            name="title",
            field=models.CharField(max_length=256),
        ),
    ]
