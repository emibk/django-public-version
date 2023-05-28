from django.shortcuts import render, redirect, get_object_or_404
from workouts.forms import UserInfoForm
from workouts.models import UserInfo
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def change_profile(request, username):
    user = get_object_or_404(User, username=username)
    user_info = UserInfo.objects.get(user=user)
    
    if request.method == 'POST':
        form = UserInfoForm(request.POST, request.FILES, instance = user_info)
        if form.is_valid():
            form.save()
            return redirect("/profile/"+username)
    else:
        copy_info = user_info
        copy_info.profile_image = None
        
        form = UserInfoForm(instance=copy_info)
    
    return render(request, 'profiles/edit_profile.html', {'form':form})
