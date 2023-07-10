from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Shoe

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def explore_page(request):
    # sorting based on user query
    sort_by = request.GET.get('sort')
    # default sort
    sort_order = 'brand'
    if (sort_by):
        sort_order = sort_by
    # all shoes except the users
    shoes = Shoe.objects.exclude(user=request.user).order_by(sort_order)
    return render(request, 'shoes/explore_page.html', {'shoes': shoes})

# logged in users collection
@login_required
def my_collection(request):
    # filters only shoes that user has
    # shoes = Shoe.objects.filter(user=username)
    shoes = Shoe.objects.filter(user=request.user)
    value = 0.0
    for shoe in shoes:
        value += shoe.price
    return render(request, 'shoes/collection.html', {'shoes': shoes, 'value': value})


# other user's collection
@login_required
def users_collection(request, username):
    # Get the user object based on the username
    user = User.objects.get(username=username)
    # Get the shoes for the user
    shoes = Shoe.objects.filter(user=user)
    return render(request, 'shoes/users_collection.html', {'shoes': shoes, 'username': username})

@login_required
def shoe_details(request, shoe_id):
    shoe = Shoe.objects.get(id=shoe_id)
    num_likes = shoe.likes.count()
    if request.method == 'POST' and request.user.is_authenticated:
        if request.user not in shoe.likes.all():
            shoe.likes.add(request.user)
            shoe.save()
    user = request.user
    return render(request, 'shoes/details.html', {'shoe': shoe, 'user': user, 'num_likes': num_likes})

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

def like_shoe(request, shoe_id):
    if request.method == 'POST':
        shoe = Shoe.objects.get(id=shoe_id)
        if request.user not in shoe.likes.all():
            shoe.likes.add(request.user)
            shoe.save()
    return redirect('details', shoe_id=shoe_id)
