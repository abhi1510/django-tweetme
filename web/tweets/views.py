import time

from django.http import StreamingHttpResponse

from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import Tweet, Notification
from .serializers import TweetSerializer

class TweetViewset(viewsets.ModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    permission_classes = [AllowAny]
    

def notifications(request):
    def event_stream():
        while True:
            time.sleep(3)
            notification = Notification.objects.filter(sent=False).first()
            if notification:
                text = notification.tweet.content
                notification.sent = True
                notification.save()
                print(f'Sent notification. Id: {notification.id}')
                yield f"data: {text}\n\n"
    return StreamingHttpResponse(event_stream(), content_type='text/event-stream')

