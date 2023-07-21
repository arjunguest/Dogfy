from rest_framework import serializers
from PasteLockly.models import Snippet

class SnippetSerializer(serializers.ModelSerializer):
    content = serializers.CharField(max_length=1000, style={'base_template': 'textarea.html', 'rows': 10})
    secret_key = serializers.CharField(max_length=100, required=False, allow_blank=True, allow_null=True, style={ 'placeholder': 'secret_key (optional)'})
    
    class Meta:
        model = Snippet
        fields = ['content', 'secret_key']
    
class ViewSnippetSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Snippet
        fields = '__all__'
       