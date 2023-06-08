from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from workouts.forms import ContactForm
from django.core.mail import send_mail
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group

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
            content = f"Email: {email}\n\nMesaj: {text}"

            print(email)
            sender_email = email
            recipient_email = 'chisimemilia@example.com'

            send_mail(
                subject,
                content,
                email, 
                [recipient_email],
                fail_silently=False
            )
            return render(request, 'contact/contact_form_sent.html')
    else:
       
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})
