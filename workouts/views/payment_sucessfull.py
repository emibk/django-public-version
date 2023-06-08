
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required


@login_required
@user_passes_test(lambda user: user.groups.filter(name='Utilizator').exists())
def payment_successful_view(request):
    return render(request, 'payment/payment_successful.html')
