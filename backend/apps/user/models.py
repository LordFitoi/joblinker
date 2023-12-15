from django.db import models
from django.db.models.signals import post_save
from django.urls import reverse
from django.dispatch import receiver
from backend.apps.utils.models import AbstractBaseModel


class Profile(AbstractBaseModel):
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)
    skills = models.ManyToManyField("jobpost.Category", blank=True)
    photo = models.ImageField("Profile Photo", blank=True, null=True)
    is_visible = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "profiles"


    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.user.username})

    @receiver(post_save, sender="auth.User")
    def create_user_profile(sender, instance, created, **_):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender="auth.User")
    def save_user_profile(sender, instance, **_):
        instance.profile.save()

    def __str__(self):
        return str(self.user)
