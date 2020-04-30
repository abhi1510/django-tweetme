from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import Tweet
from .serializers import TweetSerializer

class TweetViewset(viewsets.ModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    permission_classes = [AllowAny]
    


