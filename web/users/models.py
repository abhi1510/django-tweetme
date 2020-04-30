from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

User = settings.AUTH_USER_MODEL


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to='users', null=True, blank=True)
    location = models.CharField(max_length=250, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    followers = models.ManyToManyField(User, blank=True, related_name='following')

    def __str__(self):
        return f'{self.user} profile' 


@receiver(post_save, sender=User)
def post_user_save_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()