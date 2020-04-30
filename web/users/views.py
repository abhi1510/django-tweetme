from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from .forms import SignUpForm


def signup_view(request):
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('/')
    return render(request, 'users/sign-up.html', {'form': form})


def profile_view(request):
    profile = request.user.profile
    return render(request, 'users/profile.html', {'profile': profile})
