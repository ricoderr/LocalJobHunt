from django.urls import path 
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    # path('resume/', views.ResumeAPIView.as_view()), 
    path('debug/', views.ResumeAPIView.as_view())
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)