from django.shortcuts import render, get_object_or_404
from workouts.models import UserInfo, Follow
from django.contrib.auth.models import User
from PIL import Image
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required

@login_required
@user_passes_test(lambda user: user.groups.filter(name='Utilizator').exists())
def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    user_info = UserInfo.objects.get(user=user)
    is_following = Follow.objects.filter(follower=request.user, following=user).exists()
    print(is_following)
    
    if user_info.profile_image:
        img = Image.open(user_info.profile_image.path)

        original_width, original_height = img.size
        aspect_ratio = original_width / original_height

        new_width = 500
        new_height = int(new_width / aspect_ratio)

        img = img.resize((new_width, new_height), Image.LANCZOS)

        img.save(user_info.profile_image.path)

        user_info.profile_pic = user_info.profile_image.name
        user_info.save()

    context = {
        'user_info': user_info,
        'is_following': is_following,
        'username': username
        }
    
    return render(request, 'profiles/profile.html', context)