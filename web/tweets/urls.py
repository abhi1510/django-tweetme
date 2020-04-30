from rest_framework.routers import DefaultRouter

from .views import TweetViewset

router = DefaultRouter()
router.register(r'api/tweets', TweetViewset, basename='tweets')
urlpatterns = router.urls