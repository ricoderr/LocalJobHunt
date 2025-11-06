from django.urls import path 
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('signup/', views.SignupAPIView.as_view()),
    path('login/', views.LoginAPIView.as_view()),
    path('verify-otp/', views.VerifyOtpAPIView.as_view()), 
    path('refresh/', TokenRefreshView.as_view()), 
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)