from django.shortcuts import render
from django.http import JsonResponse
from django.core.serializers import serialize

# Create your views here.


def index(request):
    data = {"slackUsername": "Og_Vector", "backend": True, "age": 20,
            "bio": "I am a python developer, I use Django and django rest framework for Backend web deveopment"}
    return JsonResponse(data)
