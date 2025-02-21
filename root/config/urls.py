from django.contrib import admin
from django.urls import path, include
from cinema.views import home_request
from users.views import register, verify_email

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", home_request, name='home'),
    path("register/", register, name='register'),
    path("verify-email/<str:uidb64>/<str:token>/", verify_email, name="verify-email"),
]
