from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from workouts.models import Follow, Post
from django.core.paginator import Paginator
from workouts.models import Comment
from workouts.forms import CommentForm
from django.contrib.auth.models import User
from workouts.models import Reaction

@login_required

@login_required
def followings_posts(request, username):
    user = User.objects.get(username=username)
    followings = Follow.objects.filter(follower=request.user)
    followings_posts = Post.objects.filter(user__in=followings.values_list('following', flat=True)).order_by('-time')
    paginator = Paginator(followings_posts, 10)
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    post_comments = {}
    post_reactions = {}
    for post in page_obj:
        comments = Comment.objects.filter(post=post)
        post_comments[post.id] = comments
        reactions = Reaction.objects.filter(post=post).count()
        post_reactions[post.id] = reactions
    context = {
        'user': user,
        'posts': page_obj,
        'post_reactions': post_reactions,
        'post_comments': post_comments,
        'page_obj': page_obj,
        'username': username,
        'form': CommentForm(),
        'source_view': 'followings_posts'
    }
    return render(request, 'posts/followings_posts.html', context)
    