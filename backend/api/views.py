from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response


class CheckurlAPIView(APIView): 
    def get(self, request): 
        return Response({"message": "rest worked successfully!"})