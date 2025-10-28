from django.shortcuts import render
from django.http import HttpResponse

def check_url(request): 
    return HttpResponse("Api url is working fine. ")
