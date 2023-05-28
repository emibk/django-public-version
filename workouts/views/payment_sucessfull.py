
from django.shortcuts import render

def payment_successful_view(request):
    return render(request, 'payment/payment_successful.html')
