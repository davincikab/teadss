from django.conf import settings
from django.urls import path
from .views import map_view, index, forum, noticeboard, report

urlpatterns = [
    path('', index , name="home"),
    path('map/', map_view, name="map"),
    path('forum/', forum, name="forum"),
    path('noticeboard/', noticeboard, name="noticeboard"),
    path('report/', report, name="report"),
]

