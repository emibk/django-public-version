from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.shortcuts import redirect, render
from workouts.forms import RegisterForm
def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm()
    elif request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            if user is not None:
                login(request, user)
                return redirect(reverse('workouts'))
            else:
                error_msg = "Invalid email or password. Please try again."
                return render(request, 'registration/register.html', {'form': form, 'error_msg': error_msg})
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})
