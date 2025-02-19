from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.conf import settings
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(label="Usuario", max_length=150)
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    
class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
        
    def save(self, commit=True):
        user = User.objects.create_user(username=self.cleaned_data['email'], email=self.cleaned_data['email'], password=self.cleaned_data["password1"], is_active=False)
        self.send_confirmation_email(user)
        return user
    
    def send_confirmation_email(self, user):
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
        to_email = self.cleaned_data['email']
        email = EmailMessage(mail_subject, message, to=[to_email])
        email.content_subtype = "html"
        email.send()