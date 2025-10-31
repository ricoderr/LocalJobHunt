from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import LoginSerializer, SignupSerializer, VerifyOtpSerializer
from django.utils import timezone
from .utils import generate_otp

class LoginAPIView(APIView): 
    def post(self, request):
        serializer = LoginSerializer(data = request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            return Response({
                "message": "Login Successful", 
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