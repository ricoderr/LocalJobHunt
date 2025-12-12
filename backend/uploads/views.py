from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from .serializers import ResumeSerializer
from .models import Resume
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
from .storage_backends import drive_upload

class ResumeAPIView(APIView):
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ResumeSerializer(data= request.data)
        user = request.user
        if serializer.is_valid():
            file = serializer.validated_data['file']
            drive = drive_upload(file, settings.RESUME_DRIVE_FOLDER_ID)
            
            Resume.objects.update_or_create(user=user, defaults={"drive_link": drive.get('link')})
            return Response({
                'file_name': file.name,
                'content_type': file.content_type,
                'size_bytes': file.size,
                'direct_link': drive.get('direct_link'),
                'thumbnail_link': drive.get('thumbnail_link'), 
                'download_link': drive.get('download_link'),  
                "drive_id": drive.get('id'),
                
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
