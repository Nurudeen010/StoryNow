from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .serializer import Detail_Serializer
from .models import Detail



def story_view(request):
    now = Detail.objects.all()
    serializer = Detail_Serializer(now, many=True)
    new_data = serializer.data

    return JsonResponse(new_data, safe=False)
    
