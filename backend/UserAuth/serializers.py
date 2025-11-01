from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Otp
from django.utils import timezone

User = get_user_model()

class SignupSerializer(serializers.ModelSerializer): 
    phone_number = serializers.CharField(max_length=15)
    class Meta: 
        model = User
        fields = ["Fname", "Lname", "email", "phone_number", "password"]
        extra_kwargs = {"password": {"write_only": True}}
        
        
    def create(self, validated_data): 
        inactive_email_user = self.context.get('inactive_email_user')
        inactive_phone_user = self.context.get('inactive_phone_user')
        
        if inactive_email_user:
            inactive_email_user.delete()
            
        if inactive_phone_user:
            inactive_phone_user.delete()
            
        user = User.objects.create_user(
            Fname = validated_data['Fname'],
            Lname = validated_data['Lname'],
            email = validated_data.get('email'),  # .get() returns None if no value is there!
            phone_number=validated_data.get('phone_number'),
            password = validated_data['password'],
        )
        
        return user
    

class LoginSerializer(serializers.Serializer): 
    
    identifier = serializers.CharField()
    password = serializers.CharField(write_only=True)
    
    def validate(self, attrs):
        identifier = attrs.get("identifier")
        password = attrs.get("password")
        
        if not identifier or not password: 
            raise ValueError("Identifier and password both are required!")
        
        if '@' in identifier:                                         # checks whether the identifier is email or ph_number
            user = User.objects.filter(email=identifier).first()
        else: 
            user = User.objects.filter(phone_number = identifier).first()
        
        if not user:                                                  # checks if the user with these cred.. exists or not.
            raise serializers.ValidationError("User doesn't exists with these credentials!")

        if not user.check_password(password):                         # checks the password
            raise serializers.ValidationError("Incorrect password.")
        
        attrs['user'] = user        # includes user key in attrs if the user is validated
        return attrs                # returns the attrs to send back to the client. 
    
    
    '''This serializer (GenerateOtpSerializer) was required for Gen-otp endpoint but we are no longer using the endpoint else, /auth/signup only so this is not required!'''
    
# class GenerateOtpSerializer(serializers.Serializer): 
#     phone_number = serializers.CharField()
    
#     def validate_email(self, value): 
#         user_exists = User.objects.filter(phone_number=self.value).exists()
#         if not user_exists: 
#             return serializers.ValidationError("User with this phone number doesn't exists.")
#         return value
    

    
    
    
class VerifyOtpSerializer(serializers.Serializer): 
    phone_number = serializers.CharField()
    code = serializers.CharField()
    def validate(self, attrs): 
        phone_number = attrs.get('phone_number')
        code = attrs.get('code')
        
        # To check if given user exists or not
        try: 
            user = User.objects.get(phone_number=phone_number)
        except User.DoesNotExist: 
            raise serializers.ValidationError("User with this number doesn't exists!")
        
        # To check if given otp exists or not
        try: 
            otp_instance = Otp.objects.get(user=user, code = code)
        except Otp.DoesNotExist: 
            raise serializers.ValidationError("Invalid OTP!")
        
        if otp_instance.expiry_at < timezone.now(): 
            raise serializers.ValidationError("OTP expired!")
        
        attrs['user'] = user
        attrs['otp_instance'] = otp_instance
        return attrs