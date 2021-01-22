from django.conf import settings
from django.urls import path
from .views import map, index

urlpatterns = [
    path('', index , name="home"),
    path('map', map , name="map"),
]

