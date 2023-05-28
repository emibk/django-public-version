from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from workouts.models import Follow
from django.contrib.auth.models import User

@login_required
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
