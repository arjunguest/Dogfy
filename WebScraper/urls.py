from django.urls import path
from WebScraper import views
from django.conf import settings

app_name = 'WebScraper'
urlpatterns = [
    path('get_html/',views.GetHtmlContentView.as_view(), name='create_Snippet_Urls'),
]