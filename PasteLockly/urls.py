from django.urls import path
from PasteLockly import views
from django.conf import settings

app_name = 'PasteLockly'
urlpatterns = [
    path('pastelockly/',views.CreateSnippetView.as_view(), name='create_Snippet_Urls'),
    path('content/<int:pk>',views.RetriveSnippetView.as_view(), name='get_content'),
]