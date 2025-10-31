from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import LoginSerializer, SignupSerializer

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
            serializer.save()
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        