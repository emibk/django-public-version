from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from workouts.forms import FollowForm, UnfollowForm
from django.contrib.auth.models import User
from workouts.models import Follow

@login_required
def follow_view(request, username):
    user = get_object_or_404(User, username=username)

    if request.method == 'POST':
        form = FollowForm(request.POST)
        if form.is_valid():
            follow = form.save(commit=False)
            follow.follower = request.user
            follow.following = user
            follow.save()
            messages.success(request, f'You are now following {user.username}.')
            return redirect(reverse('profile_view', args=[user.username]))
    else:
        form = FollowForm()

    context = {
        'user': user,
        'form': form,
    }

    return render(request, 'profiles/profile.html', context)

@login_required
def unfollow_view(request, username):
    user = get_object_or_404(User, username=username)

    if request.method == 'POST':
        form = UnfollowForm(request.POST)
        if form.is_valid():
            Follow.objects.filter(follower=request.user, following=user).delete()
            messages.success(request, f'You have unfollowed {user.username}.')
            return redirect(reverse('profile_view', args=[user.username]))
    else:
        form = UnfollowForm()

    context = {
        'user': user,
        'form': form,
    }

    return render(request, 'profiles/profile.html', context)
