# Generated by Django 4.2 on 2023-12-13 22:13
from django.db import migrations


def create_users_profile(apps, _):
    Profile = apps.get_model('user', 'Profile')
    User = apps.get_model('auth', 'User')

    for user in User.objects.all():
        Profile.objects.create(user=user)
    

class Migration(migrations.Migration):
    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_users_profile, migrations.RunPython.noop)
    ]
