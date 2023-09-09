# Generated by Django 4.2 on 2023-09-08 17:32

from django.db import migrations


def delete_duplicated(jobposts):
    jobposts.pop(0)

    for jobpost in jobposts:
        jobpost.delete()

def join_duplicated_companies(apps, schema_editor):
    JobPost = apps.get_model('jobpost', 'JobPost')
    origin_urls = JobPost.objects.order_by().values('origin_url').distinct()

    for data in origin_urls:
        jobposts = list(JobPost.objects.filter(origin_url=data['origin_url']).order_by('created_at'))

        if len(jobposts) < 1:
            continue

        delete_duplicated(jobposts)
        

class Migration(migrations.Migration):
    dependencies = [
        ("jobpost", "0007_join_duplicated_companies"),
    ]

    operations = [
        migrations.RunPython(join_duplicated_companies, migrations.RunPython.noop)
    ]