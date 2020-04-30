from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.utils.http import is_safe_url
from django.conf import settings

from .forms import SignUpForm

ALLOWED_HOSTS = settings.ALLOWED_HOSTS


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
    user = request.user
    profile = user.profile
    from django.contrib.auth.models import User
    follow = User.objects.all()
    if request.method == 'POST':
        user.email = request.POST.get('email')
        user.username = request.POST.get('username')
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.save()
    return render(request, 'users/profile.html', {
        'user': user, 'profile': profile, 'follow': follow
    })

def follow_unfollow(request):
    _next = request.POST.get('_next')
    action = request.POST.get('action')
    who_id = request.POST.get('who_id')
    whom_id = request.POST.get('whom_id')

    who_user = get_object_or_404(User, id=who_id)
    whom_user = get_object_or_404(User, id=whom_id)
    if action == 'follow':
        who_user.following.add(whom_user.profile)
    if action == 'unfollow':
        who_user.following.remove(whom_user.profile)
    if _next and is_safe_url(_next, ALLOWED_HOSTS):
        return redirect(_next)
    return redirect('profile')


def explore_users(request, pk):
    query = request.GET.get('q')
    current_user = get_object_or_404(User, id=pk)
    if query:
        all_users = User.objects.filter(username__icontains=query)
    else:
        all_users = User.objects.all().exclude(id=pk)

    if request.method == 'POST':
        add_id = request.POST.get('add_id')
        current_user.following.add(User.objects.get(id=add_id).profile)
   
    following = [p.user for p in current_user.following.all()]
    following_ids = [f.id for f in following]
    not_following = all_users.exclude(id__in=following_ids)

    return render(request, 'users/users.html', {
        'current_user': current_user, 'following': following, 'not_following': not_following
    })