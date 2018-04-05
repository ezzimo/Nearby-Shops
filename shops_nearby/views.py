from .models import Shop, User
from .forms import SignUpForm
from django.views import generic
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.gis.db import models as gis_models
from django.contrib.gis.db.models.functions import Distance as D
from django.contrib.gis.geos import Point
from django.shortcuts import render, redirect
from django.contrib.gis.geos import *

# Create your views here.
@login_required
def home(request):
    """
    View function for home page of site.
    """
    shop_list = Shop.objects.all()
    user = User.objects.get(email=request.user)
    preferred_list = user.preferred.all()
    disliked_list = user.disliked.all()
    ref_location = user.maplocation
    shop_order = Shop.objects.annotate(distance=D('location', ref_location)).order_by('distance')

    # Number of visits to this view, as counted in the session variable.
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1
    # Render the HTML template home.html with the data in the context variable
    return render(
        request,
        'home.html',
        context={'num_visits':num_visits, 'shop_list':shop_list, 'preferred_list': preferred_list, 'disliked_list': disliked_list, 'shop_order': shop_order, 'ref_location': ref_location},
    )

@login_required
def favorites(request):
    """
    View of the preferred shop list
    """
    user = User.objects.get(email=request.user)
    preferred_list = user.preferred.all()
    return render(
        request,
        'FavoritShops.html',
        context={'preferred_list': preferred_list},
    )

@login_required
def dislikes(request):
    """
    View of the disliked shop list
    """
    user = User.objects.get(email=request.user)
    disliked_list = user.disliked.all()
    return render(
        request,
        'DislikedSops.html',
        context={'disliked_list': disliked_list},
    )



def change_preferred(request, operation, id):
    shop = Shop.objects.get(id=id)
    if operation == 'add':
        User.make_preferred(request.user, shop)
        return redirect('home')
    elif operation == 'remove':
        User.remove_preferred(request.user, shop)
        return redirect('favorites')

def change_disliked(request, operation, id):
    shop = Shop.objects.get(id=id)
    if operation == 'add':
        User.make_dislike(request.user, shop)
        return redirect('home')
    elif operation == 'remove':
        User.remove_dislike(request.user, shop)
        return redirect('home')



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect('/shops_nearby')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
