from django import forms

class PaymentForm(forms.Form):
    stripeToken = forms.CharField() 
    
