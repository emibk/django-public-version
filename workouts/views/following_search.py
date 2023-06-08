from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from workouts.models import Follow


from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group
@login_required
@user_passes_test(lambda user: user.groups.filter(name='Utilizator').exists())
def following_search(request):
    query = request.GET.get('query')
    users = User.objects.filter(username__icontains=query).exclude(id=request.user.id)
    context = {
        'users': users,
        'query': query,
    }
    return render(request, 'follows/following_search_results.html', context)

