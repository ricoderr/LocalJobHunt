from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import LoginSerializer, SignupSerializer, VerifyOtpSerializer
from django.utils import timezone
from django.contrib.auth import get_user_model
from .utils import generate_otp
from rest_framework_simplejwt.tokens import RefreshToken

class LoginAPIView(APIView): 
    def post(self, request):
        serializer = LoginSerializer(data = request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            refresh = RefreshToken.for_user(user)
            access = refresh.access_token
            return Response({
                "message": "Login Successful", 
                "tokens": {
                    "access" : str(access),
                    "refresh": str(refresh), 
                },
                "user_data": {
                    "id": user.id,
                    "Fname": user.Fname,
                    "Lname": user.Lname,
                    "email": user.email,
                    "phone_number": user.phone_number
                }
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)


class SignupAPIView(APIView): 
    def post(self, request): 
        email = request.data.get('email')
        phone = request.data.get('phone_number')
        User = get_user_model()
        # Delete any inactive user with the same email
        try:
            user = User.objects.get(email=email, is_active=False)
            user.delete()
        except User.DoesNotExist:
            pass

        # Delete any inactive user with the same phone number
        try:
            user = User.objects.get(phone_number=phone, is_active=False)
            user.delete()
        except User.DoesNotExist:
            pass
        serializer = SignupSerializer(data = request.data)
        if serializer.is_valid(): 
            user = serializer.save()
            generate_otp(user=user)
            return Response(
                {"message": "A verification message is sent to the phone number."}, status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
        
class VerifyOtpAPIView(APIView):  
    def post(self, request): 
        serializer = VerifyOtpSerializer(data=request.data)
        if serializer.is_valid(): 
            user = serializer.validated_data['user']
            otp_instance = serializer.validated_data['otp_instance']
            
            # verify the user's phone-number by activating the user. 
            user.is_active = True 
            user.verified_at = timezone.now()
            user.save()
            
            # delete the otp after being used
            otp_instance.delete()
            
            return Response({"message": "OTP verified Successfully!", 
                             "user_data": {
                                 "Fname": user.Fname , 
                                 "Lname": user.Lname , 
                                 "email": user.email , 
                                 "phone_number": user.phone_number, 
                                 
                             }
                             },status= status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST )