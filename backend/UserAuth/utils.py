from random import randint 
from .models import Otp
from django.utils import timezone
from datetime import timedelta
from twilio.rest import Client
import os 
from dotenv import load_dotenv

load_dotenv()


def generate_otp(user): 
    
    account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
    auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
    from_number = os.environ.get("TWILIO_PHONE_NUMBER")
    
    code = str(randint(100000,999999))
    otp, created = Otp.objects.update_or_create(user=user, defaults={
        'code': code, 'expiry_at': timezone.now() + timedelta(minutes=10)
    })
    
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=f"You Verification OTP for LocalJobHunt is {code}. This will expire in 10 minutes.", 
        from_=from_number, 
        to = user.phone_number
    )
    
    print(user, code, created)
    return message.sid

