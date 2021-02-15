from django.conf import settings
from django.urls import path
from .views import map_view, index, forum, noticeboard, report, get_reported_issues

urlpatterns = [
    path('', index , name="home"),
    path('map/', map_view, name="map"),
    path('forum/', forum, name="forum"),
    path('noticeboard/', noticeboard, name="noticeboard"),
    path('report/', report, name="report"),
    path('get_reported_issues/',get_reported_issues, name="reported-issues"),
]

