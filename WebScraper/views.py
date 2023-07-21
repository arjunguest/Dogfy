from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from rest_framework.reverse import reverse
from rest_framework import status
import json

from WebScraper.tasks import get_table_data
class GetHtmlContentView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'urlshortener/htmltable.html'
    
    def get(self, request):
        webpage_url = 'https://www.nseindia.com/'
        obj = get_table_data.delay(webpage_url)
        return Response({'message':obj})
