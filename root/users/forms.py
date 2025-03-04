from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.conf import settings
from users.tasks import process_send_confirmation_email

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
        if settings.APPLY_ASYNC:
            print("Se ha enviado asincronamente.")
            process_send_confirmation_email.apply_async(
                args = [user.pk]
            )
        else:
            print("Se ha enviado de manera sincrona.")
            process_send_confirmation_email.apply(
                args = [user.pk]
            )