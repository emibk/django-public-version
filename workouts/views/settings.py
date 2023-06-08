from workouts.forms import EmailUpdateForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def settings(request):
    user = request.user
    if request.method == 'POST':
        form = EmailUpdateForm(request.POST)
        if form.is_valid():
            new_email = form.cleaned_data['new_email']
            user.email = new_email
            user.save()
            return redirect('settings')
    else:
        form = EmailUpdateForm(initial={'new_email': user.email})

    return render(request, 'settings/settings.html', {'user': user, 'form': form})
