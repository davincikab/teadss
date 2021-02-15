from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize

from django.contrib.gis.geos import GEOSGeometry
# 3rd party
import json

# local code
from .forms import NoticeBoardForm, FarmerIssueForm
from .models import NoticeBoard, FarmerIssue

# Create your views here.
def index(request):
    return render(request, 'index.html', {'section':'home'})

def map_view(request):
    return render(request, 'decisionsupport/map.html', {'section':'map'})

def forum(request):
    return render(request, 'decisionsupport/forum.html', {'section':'forum'})

def report(request):
    if request.method == "POST":
        coord = request.POST.get('geom')
        geom = f'POINT({coord})'

        print(request.POST)
        form = FarmerIssueForm(request.POST)

        if form.is_valid():
            issue = form.save(commit=False)
            issue.geom = GEOSGeometry(geom)
            issue.save()

            return HttpResponse(json.dumps({'message':'success'}))
        else:
            print(form.errors)
            return HttpResponse(json.dumps({'errors':form.errors}))
    else:
        form = FarmerIssueForm()
    
    context = {
        'section':'report',
        'form':form,
    }
    return render(request, 'decisionsupport/report.html', context)

def get_reported_issues(request):
    issues = serialize('geojson', FarmerIssue.objects.all())

    return HttpResponse(json.dumps({'location':issues}))

def noticeboard(request):
    notices = NoticeBoard.objects.all()
    if request.GET.get('title', None):
        title = request.GET.get('title')
        notices = NoticeBoard.objects.filter(title__icontains=title)

    if request.method == "POST":
        form = NoticeBoardForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

            return redirect("/noticeboard")
    else:
        form = NoticeBoardForm()
    
    context = {
        'form':form,
        'notices':notices,
        'section':'notice'
    }

    return render(request, 'decisionsupport/noticeboard.html', context)