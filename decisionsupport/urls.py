from django.conf import settings
from django.urls import path
from .views import map_view, index, forum

urlpatterns = [
    path('', index , name="home"),
    path('map/', map_view, name="map"),
    path('forum', forum, name="forum"),
]

