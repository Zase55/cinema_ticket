from django.http import HttpResponse
from django.shortcuts import render, redirect
from users.forms import CustomUserCreationForm
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import login

# Create your views here.
def register(request):
    data = {
        'form': CustomUserCreationForm()
    }
    
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(to='home')
        data['form'] = formulario
    
    return render( request, 'registration/register.html', data )

def verify_email(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
        if default_token_generator.check_token(user, token):
            user.is_active=True
            user.save()
            login(request, user)
            return redirect(to='home')
    except Exception as e:
        return HttpResponse({'errors':e}, content_type='application/json')