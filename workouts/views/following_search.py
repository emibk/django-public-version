from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from workouts.models import Follow


from django.urls import reverse

@login_required
def following_search(request):
    query = request.GET.get('query')
    users = User.objects.filter(username__icontains=query).exclude(id=request.user.id)
    context = {
        'users': users,
        'query': query,
    }
    return render(request, 'follows/following_search_results.html', context)

