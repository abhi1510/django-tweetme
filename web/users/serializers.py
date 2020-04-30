from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    avatar = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'avatar', 'is_active', 
            'is_staff', 'is_superuser', 'user_permissions', 'groups', 'last_login', 'date_joined',)

    def get_avatar(self, obj):
        avatar = obj.profile.avatar
        if avatar:
            return avatar.url
        return None