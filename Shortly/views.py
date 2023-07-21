from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from rest_framework import status
from django.utils import timezone
import json

# Models 
from Shortly.models import Urls

#serializers
from Shortly.serializers import UrlSerializer

from Shortly.utils import generate_short_code

class CreateShortUrlsView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'urlshortener/Urls.html'
    
    def post(self, request):
        try:
            serializer = UrlSerializer(data=request.data)
            if serializer.is_valid():
                long_url = serializer.validated_data['long_url']
                short_code = generate_short_code()
                while Urls.objects.filter(short_url=short_code).exists():
                    short_code = generate_short_url()
                short_url = Urls.objects.create(long_url=long_url, short_url=short_code)
                return Response({'serializer': serializer, 'short_url': short_url},status=status.HTTP_201_CREATED)
            else:
                return Response({'message': ' Please fill vaild data'}, status = status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'message': str(e)}, status = status.HTTP_400_BAD_REQUEST)
        
    def get (self,request):
        try:
            serializer = UrlSerializer()
            return Response({'serializer': serializer})
        except Exception as e:
            return Response({'message': str(e)}, status = status.HTTP_400_BAD_REQUEST)

class PreviewShortUrlsView(APIView):
    def get (self,request,short_code):
        try:
            shortened_url = Urls.objects.get(short_url=short_code)
            if shortened_url:
                return HttpResponseRedirect(redirect_to=shortened_url.long_url)
            else:   
                return Response({'message': ' Url not found'}, status = status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'message': str(e)}, status = status.HTTP_400_BAD_REQUEST)