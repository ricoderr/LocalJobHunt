from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class Resume(models.Model): 
    file = models.FileField(null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    drive_link = models.CharField(max_length=225, null=True)