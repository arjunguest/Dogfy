from django.urls import path
from Shortly import views
from django.conf import settings

app_name = 'Shortly'
urlpatterns = [
    path('short_url/',views.CreateShortUrlsView.as_view(), name='Create_Short_Urls'),
    path('short_url/<str:short_code>',views.PreviewShortUrlsView.as_view(), name='get_Short_Urls'),
]