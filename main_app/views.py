from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Shoe

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def explore_page(request):
    # all shoes except the users
    shoes = Shoe.objects.exclude(user=request.user)
    return render(request, 'shoes/explore_page.html', {'shoes': shoes})

@login_required
def collection(request):
    # filters only shoes that user has
    shoes = Shoe.objects.filter(user=request.user)
    return render(request, 'shoes/collection.html', {'shoes': shoes})

@login_required
def shoe_details(request, shoe_id):
    shoe = Shoe.objects.get(id=shoe_id)
    user = request.user
    return render(request, 'shoes/details.html', {'shoe': shoe, 'user': user})

class ShoeCreate(LoginRequiredMixin, CreateView):
    model = Shoe
    fields = ['brand', 'modelName', 'type', 'colorway', 'description', 'year', 'price', 'img']
    def form_valid(self, form):
    # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user  # form.instance is the shoe
    # Let the CreateView do its job as usual
        return super().form_valid(form)
    
class ShoeUpdate(LoginRequiredMixin, UpdateView):
    model = Shoe
    fields = ['brand', 'modelName', 'type', 'colorway', 'description', 'year', 'price', 'img']

class ShoeDelete(LoginRequiredMixin, DeleteView):
    model = Shoe
    success_url = '/collection'


def signup(request):
    errorMsg = ''
    if (request.method == 'POST'):
        form = UserCreationForm(request.POST)
        if (form.is_valid()):
            user = form.save()
            login(request, user)
            return redirect('collection')
        else:
            errorMsg = 'Invalid sign up. Please try again.'
    form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form, 
        'errorMsg': errorMsg,
    })
