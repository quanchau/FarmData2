from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.generic import CreateView,ListView,DetailView
from django.utils.decorators import method_decorator


from .forms import *
from .models import *

# Create your views here.

@login_required
def index(request):
    return render(request,'farmdb/index.html')


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request,'farmdb/index.html')
            else:
                return render(request, 'farmdb/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'farmdb/login.html', {'error_message': 'Invalid username or password'})
    return render(request, 'farmdb/login.html')

def logout_user(request):
    logout(request)
    return render(request, 'farmdb/login.html', {'logout': 'True'})

def create_farmer(request):
    form = FarmerForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse("<html><body><h1>Welcome, {}</h1></body></html>".format(user.first_name))
                #Do what needs to be done after a user logs in
    context = {
        "form": form,
    }
    return render(request, 'farmdb/register.html', context)



# CreateViews

@method_decorator(login_required, name='dispatch')
class AnimalGroupCreateView(CreateView):
    template_name = "farmdb/createView/create_animalGroup.html"
    model = AnimalGroup
    fields = ('animalGroup',)
    success_url = '/'

    def form_valid(self, form):
        # Assign the farm from request.user
        form.instance.farm = self.request.user.farmer.farm
        form.instance.active = True
        return super(AnimalGroupCreateView, self).form_valid(form)


# ListViews

@method_decorator(login_required, name='dispatch')
class AnimalGroupListView(ListView):
    model = AnimalGroup
    template_name = 'farmdb/listView/animalGroup_list.html'


    def get_queryset(self):
        return AnimalGroup.objects.filter(farm=self.request.user.farmer.farm)







