from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import TweetViewset, notifications

router = DefaultRouter()
router.register(r'api/tweets', TweetViewset, basename='tweets')
urlpatterns = router.urls

urlpatterns += [path('notifications', notifications, name='notifications')]