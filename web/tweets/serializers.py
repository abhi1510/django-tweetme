from django.utils.timesince import timesince

from rest_framework import serializers

from .models import Tweet
from users.serializers import UserSerializer

class TweetSerializer(serializers.ModelSerializer):
    author_details = serializers.SerializerMethodField()
    timestamp = serializers.SerializerMethodField()
    
    class Meta:
        model = Tweet
        fields = ('id', 'content', 'image', 'timestamp', 'author', 'author_details')

    def get_author_details(self, obj):
        return UserSerializer(obj.author).data

    def get_timestamp(self, obj):
        return timesince(obj.timestamp)
