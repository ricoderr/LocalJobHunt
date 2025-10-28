from django.shortcuts import render
from django.http import HttpResponse

def check_url(request): 
    return HttpResponse("UserAuth url is working fine.")
