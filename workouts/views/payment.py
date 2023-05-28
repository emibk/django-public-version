import stripe
from django.conf import settings
from django.shortcuts import render
from workouts.forms import PaymentForm
from workouts.models import Payment

stripe.api_key = settings.STRIPE_SECRET_KEY

def payment_view(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            token = form.cleaned_data['stripeToken']
            try:
                payment_intent = stripe.PaymentIntent.create(
                    amount=300,
                    currency='ron',
                    payment_method=token,
                    confirm=True,  
                )
                
                if payment_intent.status == 'succeeded':
                    payment = Payment(
                        user=request.user,
                        price=300,
                        status='Paid',
                    )
                    payment.save()
                
                return render(request, 'payment/payment_successful.html')
            except stripe.error.CardError as e:
                error_message = e.error.message
                return render(request, 'payment/payment.html', {'form': form, 'error_message': error_message})
    else:
        form = PaymentForm()
    return render(request, 'payment/payment.html', {'form': form})
