from rest_framework import serializers
from Shortly.models import Urls

class UrlSerializer(serializers.Serializer):
    long_url = serializers.CharField(max_length=100,style={ 'placeholder': 'urls'})