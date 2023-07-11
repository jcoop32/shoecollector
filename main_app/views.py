from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.db.models import Q # Q object is an object used to encapsulate a collection of keyword arguments. 
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
    # sorting based on user query params
    # is a method used to retrieve the value of a specific parameter from the query string in a GET request.
    sort_by = request.GET.get('sort')
    # will look for the specified parameter name in the query string of the URL. If the parameter exists, it will return its value.
    # default sort
    sort_order = 'brand'
    if (sort_by):
        # sets sort order to user requested order from <a> in explore_page
        sort_order = sort_by
    # all shoes except the users
    shoes = Shoe.objects.exclude(user=request.user).order_by(sort_order)
    #Search 
    search_query = request.GET.get('brand')
    if search_query:
        # searches matching brand name or model name
        # https://stackoverflow.com/questions/16303735/search-through-multiple-fields-in-django
        # using __icontains to find 'LIKE' characters
        shoes = shoes.filter(Q(brand__icontains=search_query) | Q(modelName__icontains=search_query))
        # resets search_query to empty string
        search_query = ''
    return render(request, 'shoes/explore_page.html', {'shoes': shoes})

@login_required
# logged in users collection
def my_collection(request):
    # filters only shoes that user has
    # shoes = Shoe.objects.filter(user=username)
    shoes = Shoe.objects.filter(user=request.user)
    value = 0.0
    # totaling up collection value for user
    for shoe in shoes:
        value += shoe.price
    return render(request, 'shoes/collection.html', {'shoes': shoes, 'value': value})


# other user's collection
@login_required
def users_collection(request, username):
    # Get the user object based on the username selected
    user = User.objects.get(username=username)
    # Get the shoes for the user selected
    shoes = Shoe.objects.filter(user=user)
    return render(request, 'shoes/users_collection.html', {'shoes': shoes, 'username': username})

@login_required
def shoe_details(request, shoe_id):
    # getting shoeid requested
    shoe = Shoe.objects.get(id=shoe_id)
    # finding number of likes for shoe
    num_likes = shoe.likes.count()
    # 
    if request.method == 'POST':
        if request.user not in shoe.likes.all():
            shoe.likes.add(request.user)
            shoe.save()
    # getting logged in user
    user = request.user
    return render(request, 'shoes/details.html', {'shoe': shoe, 'user': user, 'num_likes': num_likes})

class ShoeCreate(LoginRequiredMixin, CreateView):
    model = Shoe
    # selected fields to add
    fields = ['brand', 'modelName', 'type', 'colorway', 'description', 'year', 'price', 'img']
    def form_valid(self, form):
    # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user  # form.instance is the shoe
    # Let the CreateView do its job as usual
        return super().form_valid(form)
    
class ShoeUpdate(LoginRequiredMixin, UpdateView):
    model = Shoe
    # selected fields to update
    fields = ['brand', 'modelName', 'type', 'colorway', 'description', 'year', 'price', 'img']

class ShoeDelete(LoginRequiredMixin, DeleteView):
    model = Shoe
    # redirects user to collection after successful deletion
    success_url = '/collection'


def signup(request):
    errorMsg = ''
    # checks if request method is post
    if (request.method == 'POST'):

        form = UserCreationForm(request.POST)
        if (form.is_valid()):
            # saves user to db
            user = form.save()
            # automatically logins user after successful signup
            login(request, user)
            # send user to collection page
            return redirect('collection')
        else:
            # if signup is invalid display error msg
            errorMsg = 'Invalid sign up. Please try again.'
    form = UserCreationForm()
    # empty form for bad POST or GET request
    # renders signup form
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
