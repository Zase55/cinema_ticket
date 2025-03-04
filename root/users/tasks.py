from django_celery.celery_instance import app
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.conf import settings
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string

@app.task()
def process_send_confirmation_email(user_pk):
    user = User.objects.get(pk=user_pk)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = default_token_generator.make_token(user)
    verification_link = (
        f'{settings.BASE_APP_URL}/verify-email/{uid}/{token}/'
    )
    mail_subject = 'Activation link has been sent to your email id'
    message = render_to_string( 'emails/confirmation_email.html', {
        'user': user,
        'domain': verification_link,
        'uid':uid,
        'token':token, })
    email = EmailMessage(mail_subject, message, to=[user.email])
    email.content_subtype = "html"
    email.send()