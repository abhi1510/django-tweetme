from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Tweet(models.Model):
    content = models.CharField(max_length=150)
    image = models.FileField(upload_to='media/tweets', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-timestamp',)

    def __str__(self):
        return self.content
