from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from cinema.views import home_request
from users.views import register, verify_email

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("pay/", include('payments.urls')),
    path("", home_request, name='home'),
    path("register/", register, name='register'),
    path("verify-email/<str:uidb64>/<str:token>/", verify_email, name="verify-email"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
