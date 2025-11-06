from django.db import models
from django.contrib.auth import get_user_model
from .storage_backends import KoofrStorage
User = get_user_model()

class Resume(models.Model): 
    file = models.FileField(storage=KoofrStorage, upload_to='resumes')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    