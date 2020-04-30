from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import signup_view, profile_view

urlpatterns = [
    path('signup', signup_view, name='sign-up'),
    path('profile', profile_view, name='profile'),
    path('login', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
]
