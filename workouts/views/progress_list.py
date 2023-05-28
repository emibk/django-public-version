from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from workouts.models import Progress
from django.contrib.auth.models import User

@login_required
def progress_list(request, username):
    user = User.objects.get(username=username)
    filter_option = request.GET.get('filter')

    progress_list = Progress.objects.filter(user=user).order_by('-id')

    if filter_option == 'date_asc':
        
        progress_list = progress_list.order_by('id')
    elif filter_option == 'date_desc':
        
        progress_list = progress_list.order_by('-id')
    return render(request, 'progress/progress.html', {'progress_list': progress_list, 'username': username,})
