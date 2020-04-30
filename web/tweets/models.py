from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

User = settings.AUTH_USER_MODEL

class Tweet(models.Model):
    content = models.CharField(max_length=150)
    image = models.FileField(upload_to='tweets', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-timestamp',)

    def __str__(self):
        return self.content


class Notification(models.Model):
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name='notification') 
    sent = models.BooleanField(default=False)

    def __str__(self):
        return self.tweet.content


@receiver(post_save, sender=Tweet)
def post_tweet_save_signal(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(tweet=instance).save()