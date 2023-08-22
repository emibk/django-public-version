from django.shortcuts import render
from workouts.models import Post
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from workouts.models import Comment
from workouts.forms import CommentForm
from workouts.models import Reaction
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required

@login_required
@user_passes_test(lambda user: user.groups.filter(name='Utilizator').exists())
def user_posts(request, username):
    user = User.objects.get(username=username)
    posts = Post.objects.filter(user=user).order_by('-time')
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    logged_user = request.user
    reacted_to_posts = logged_user.reactions.values_list('post_id', flat=True)

    context = {
        'user': user,
        'posts': page_obj,
        
        'page_obj': page_obj,
        'username': username,
        'form': CommentForm(),
        'source_view': 'user_posts',
        'reacted_to_posts': reacted_to_posts,
    }
    return render(request, 'posts/user_posts.html', context)