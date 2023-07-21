from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from rest_framework.reverse import reverse
from rest_framework import status
import json

# Models 
from PasteLockly.models import Snippet

# Serializers
from PasteLockly.serializers import SnippetSerializer

# Create your views here.
class CreateSnippetView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'urlshortener/snippet.html'
    
    def post(self, request, format=None): 
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            text = serializer.validated_data['content']
            unique_key = serializer.validated_data['secret_key']
            encrypt =False
            if unique_key:
                encrypt =True   
            text_obj = Snippet.objects.create(content=text, secret_key=unique_key, encrypt=encrypt)
            view1_url = reverse('PasteLockly:get_content',args=[text_obj.id])
            print("view1_url",view1_url)
            url = request.build_absolute_uri(view1_url)
            print("url", url)
            text_obj.url = url
            text_obj.save()
            return Response({'serializer':serializer},status=status.HTTP_201_CREATED)
        else:
            return Response({'message': ' Please fill vaild data'}, status = status.HTTP_400_BAD_REQUEST)
        
    def get (self,request):
        try:
            serializer = SnippetSerializer()
            return Response({'serializer': serializer})
        except Exception as e:
            return Response({'message': str(e)}, status = status.HTTP_400_BAD_REQUEST)
        
class RetriveSnippetView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'urlshortener/content.html'
    
    def get(self, request,pk,format=None):
        try:
            serializer = SnippetSerializer()
            snippet_obj = Snippet.objects.get(id=pk)
            if snippet_obj.encrypt == True:
                unique_key = request.GET.get('key')
                if unique_key == snippet_obj.secret_key:
                    return Response({'message':snippet_obj, 'serializer': serializer})
                else:   
                    return Response({'message': ' Invaild key'}, status = status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'message':snippet_obj, 'serializer': serializer})
        except Exception as e:
            return Response({'message': str(e)}, status = status.HTTP_400_BAD_REQUEST)