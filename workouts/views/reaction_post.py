from workouts.models import Post, Reaction
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required

@login_required
@user_passes_test(lambda user: user.groups.filter(name='Utilizator').exists())
def reaction_post(request, post_id, username):
    post = Post.objects.get(pk=post_id)
    user = request.user

    reaction_exists = Reaction.objects.filter(user=user, post=post).first()
    if reaction_exists:
        reaction_exists.delete()
    else:
        Reaction.objects.create(user=user, post=post)
    return redirect(reverse('user_posts', args=[username]) + f'#post-{post_id}')
