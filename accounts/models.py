from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        db_table = 'lms_profiles'


@receiver(models.signals.post_save, sender=User)
def create_new_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
