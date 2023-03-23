from django.shortcuts import render
from .models import *
from django.http import JsonResponse
# Create your views here.

def home(request):
    data = Posts.objects.values()

    return JsonResponse({"data": list(data)} , safe=False )

