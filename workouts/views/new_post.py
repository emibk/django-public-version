from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from workouts.models import Post, UserInfo
from workouts.forms import PostForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group

@login_required
@user_passes_test(lambda user: user.groups.filter(name='Utilizator').exists())
def create_post(request, username):
    user = User.objects.get(username=username)
    userInfo = UserInfo.objects.get(user=user)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = user
            post.text = post.text.replace('\n', '<br>')
            post.save()
            if post.post_type == 'Schimbare in greutate':
                userInfo.current_weight = post.text.split()[-2]
                userInfo.save()
            return redirect("/profile/"+username+"/posts/")
    else:
        form = PostForm()
    
    return render(request, 'posts/new_post.html', {'form': form, 'username':username})
