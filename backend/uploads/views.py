# uploads/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from .serializers import ResumeSerializer
from .models import Resume
from rest_framework.permissions import IsAuthenticated

class ResumeAPIView(APIView):
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ResumeSerializer(data= request.data)
        user = request.user
        if serializer.is_valid():
            file = serializer.validated_data['file']
            Resume.objects.update_or_create(user=user, defaults={"file": file})
            return Response({
                'file_name': file.name,
                'content_type': file.content_type,
                'size_bytes': file.size,
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
