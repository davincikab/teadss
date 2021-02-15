from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from django.views.generic import CreateView
from django.contrib.auth import login
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import FilteredRelation, Q


from .models import User
from .forms import FarmerSignUpForm, DecisonMakerSignUpForm, ProfileForm

# Create your views here.
def signup(request):
    return render(request, "account/signup.html")

class FarmerSignUpView(CreateView):
    model = User
    form_class = FarmerSignUpForm
    template_name = "account/register.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        kwargs['user_type'] = 'farmer'
        context['title'] = "Farmer Registration"
       
        return context
    
    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_farmer = True
        user.save()

        login(self.request, user)
        return redirect('home')
        

class DecisonMakerSignUpView(CreateView):
    model = User
    form_class = DecisonMakerSignUpForm
    template_name = "account/register.html"    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        kwargs['user_type'] = 'decisonmaker'
        context['title'] = "DecisonMaker Registration "

        return context
    
    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_decisionmaker = True
        user.save()

        login(self.request, user)
        return redirect('home')
   

# profile view
def profile(request):
    # determine if the username
    profile = request.user
    if request.GET.get('user', None):
        username = request.GET.get('user')
        try:
            profile = User.objects.get(username=username)
        except User.DoesNotExist:
            return HttpResponseNotFound("<p>Page not found</p>")
    
    context = {
        'profile':profile
    }

    return render(request, "account/user_profile.html", context)

def farmers_view(request):
    if request.GET.get('query'):
        query = request.GET.get('query')
        farmers = User.objects.filter(
            Q(username__icontains=query) | Q(first_name__icontains=query) | Q(last_name__icontains=query)
            ).filter(is_farmer=True)
    else:
        farmers = User.objects.filter(is_farmer=True)

    paginator = Paginator(farmers, 10)
    page = request.GET.get('page')
    farmers = paginator.get_page(page)

    context = {
        'farmers':farmers
    }

    return render(request, 'account/farmers.html', context)

def decisionmarkers_view(request):
    if request.GET.get('query'):
        query = request.GET.get('query')
        decisionmakers = User.objects.filter(
            Q(username__icontains=query) | Q(first_name__icontains=query) | Q(last_name__icontains=query)
            ).filter(is_decisionmaker=True)
    else:
        decisionmakers = User.objects.filter(is_decisionmaker=True)

    paginator = Paginator(decisionmakers, 10)
    page = request.GET.get('page')
    decisonmakers = paginator.get_page(page)

    # message obj

    context = {
        'decisionmakers':decisionmakers,

    }

    return render(request, 'account/decision_makers.html', context)

# update user profile
def update_user_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            
            # update the details manually
            user.first_name = request.POST.get('first_name')
            user.last_name = request.POST.get('last_name')
            user.phone_number = request.POST.get('phone_number')
            user.save()

            return redirect("/account/profile/")
    else:
        form = ProfileForm(instance=request.user)
    context = {
        'user_profile_form':form
    }

    return render(request, 'account/user_edit_form.html', context)