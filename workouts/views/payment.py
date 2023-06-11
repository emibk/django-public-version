import stripe
from django.conf import settings
from django.shortcuts import render
from workouts.forms import PaymentForm
from workouts.models import Payment
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
@user_passes_test(lambda user: user.groups.filter(name='Utilizator').exists() and not user.groups.filter(name='Platitor').exists())
def payment_view(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
           
            token = form.cleaned_data['stripeToken']
            try:
                payment_intent = stripe.PaymentIntent.create(
                    amount=30,
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
                    user = request.user
                    payer_group, _ = Group.objects.get_or_create(name='Platitor')
                    user.groups.add(payer_group)
                
                return render(request, 'payment/payment_successful.html')
            except stripe.error.CardError as e:
                error_message = e.error.message
                return render(request, 'payment/payment.html', {'form': form, 'error_message': error_message})
    else:
        form = PaymentForm()
    return render(request, 'payment/payment.html', {'form': form})
