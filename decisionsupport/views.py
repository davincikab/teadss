from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {'section':'home'})

def map_view(request):
    return render(request, 'decisionsupport/map.html', {'section':'map'})

def forum(request):
    return render(request, 'decisionsupport/forum.html', {'section':'forum'})