from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from workouts.models import Follow
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group

@login_required
@user_passes_test(lambda user: user.groups.filter(name='Utilizator').exists())
def my_follows(request, username):
    user_ = get_object_or_404(User, username=username)

    followings = Follow.objects.filter(follower=user_)
    followers = Follow.objects.filter(following=user_)
  
    context = {
        'followings': followings,
        'followers': followers,
        'username': username
        
    }
    return render(request, 'follows/follows.html', context)
