from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

# local code
from .forms import NoticeBoardForm
from .models import NoticeBoard

# Create your views here.
def index(request):
    return render(request, 'index.html', {'section':'home'})

def map_view(request):
    return render(request, 'decisionsupport/map.html', {'section':'map'})

def forum(request):
    return render(request, 'decisionsupport/forum.html', {'section':'forum'})

def report(request):
    return render(request, 'decisionsupport/report.html', {'section':'report'})

def get_reported_issues(request):
    return JsonResponse(json.dumps({'location':[]}))

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