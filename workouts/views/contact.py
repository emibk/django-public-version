from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from workouts.forms import ContactForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group
from django.conf import settings


@login_required
@user_passes_test(lambda user: user.groups.filter(name='Utilizator').exists())
def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            username = request.user.username
            email = form.cleaned_data['email']
            text = form.cleaned_data['text']
            
            subject = f"Contactat de {username}"
            content = f"Email: {email}\n\nMesaj {text}"
            
            
            recipient_email = 'emilia1290@outlook.com'  

            email_message = EmailMessage(
                subject,
                content,
                settings.DEFAULT_FROM_EMAIL,
                [recipient_email],
                reply_to=[email]

            )
            email_message.send()

            return render(request, 'contact/contact_form_sent.html')
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})