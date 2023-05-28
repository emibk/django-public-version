from django.shortcuts import render, get_object_or_404
from workouts.models import UserInfo, Follow
from django.contrib.auth.models import User
from PIL import Image


def profile_view(request, username):
    print(f'username = {username}')
    user = get_object_or_404(User, username=username)
    user_info = UserInfo.objects.get(user=user)
    is_following = Follow.objects.filter(follower=request.user, following=user).exists()
    print(is_following)
    
    if user_info.profile_image:
        img = Image.open(user_info.profile_image.path)

        # Get the aspect ratio of the original image
        original_width, original_height = img.size
        aspect_ratio = original_width / original_height

        # Calculate the new width and height of the resized image
        new_width = 500
        new_height = int(new_width / aspect_ratio)

        # Resize the image while maintaining the aspect ratio
        img = img.resize((new_width, new_height), Image.LANCZOS)

        # Overwrite the original image with the resized image
        img.save(user_info.profile_image.path)

        # Update profile picture file path in UserInfo object
        user_info.profile_pic = user_info.profile_image.name
        user_info.save()

    context = {
        'user_info': user_info,
        'is_following': is_following,
        'username': username
        }
    
    return render(request, 'profiles/profile.html', context)