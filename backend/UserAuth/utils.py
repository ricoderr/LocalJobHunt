from random import randint 
from .models import Otp
from django.utils import timezone
from datetime import timedelta

def generate_otp(user): 
    code = str(randint(100000,999999))
    otp, created = Otp.objects.update_or_create(user=user, defaults={
        'code': code, 'expiry_at': timezone.now() + timedelta(minutes=10)
    })
    print(user, otp, created)
    return otp


