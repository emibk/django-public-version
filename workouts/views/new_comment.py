from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from workouts.models import Post, Comment
from workouts.forms import CommentForm
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group

@login_required
@user_passes_test(lambda user: user.groups.filter(name='Utilizator').exists())
def create_comment(request, post_id, username, view):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()

           
            return redirect(reverse(view, args=[username]) + f'#comment-{comment.id}')
            
           

    else:
        form = CommentForm()

    context = {
        'post': post,
        'form': form,  
    }

    return render(request, 'posts/'+view+'.html', context)
