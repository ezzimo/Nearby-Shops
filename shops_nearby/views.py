from .models import Shop, User
from .forms import SignUpForm
from .serializers import ShopSerializer, UserSerializer
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
from rest_framework.views import APIView, exception_handler
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.decorators import api_view
import json
from django.http import JsonResponse, HttpResponse
from django.forms.models import model_to_dict
from rest_framework import status



# Create your views here.
@login_required
@api_view(['GET', 'PUT', 'DELETE'])
def home(request, format=None):
    """
    View function for home page of site.
    """
    shop_list = Shop.objects.all() # get all the shops from db to shop_list
    user = User.objects.get(email=request.user) # get the email of the current user
    preferred_list = user.preferred.all() #get all the preferred shops for the current user
    disliked_list = user.disliked.all() #get all the disliked shops for the current user in disliked_list
    ref_location = user.maplocation # get the coordinates of the user from maplocation to ref_location
    shop_order = Shop.objects.annotate(distance=D('location', ref_location)).order_by('distance')     # Render the HTML template home.html with the data in the context variable
    return Response({'shop_order': ShopSerializer(shop_order,many=True).data,'disliked_list': ShopSerializer(disliked_list,many=True).data, 'preferred_list': ShopSerializer(preferred_list,many=True).data},)


@login_required
@api_view(['GET', 'PUT', 'DELETE'])
def favorites(request, format=None):
    """
    View of the preferred shop list
    """
    user = User.objects.get(email=request.user)
    preferred_list = user.preferred.all()
    return Response({'preferred_list': ShopSerializer(preferred_list,many=True).data},
    )

@login_required
@api_view(['GET', 'PUT', 'DELETE'])
def dislikes(request, format=None):
    """
    View of the disliked shop list
    """
    user = User.objects.get(email=request.user)
    disliked_list = user.disliked.all()
    return Response({'disliked_list': ShopSerializer(disliked_list,many=True).data},
    )


@api_view(['GET', 'PUT', 'DELETE'])
def change_preferred(request, operation, id):
    """
    add or remove shop from preferred list of shops
    """
    shop = Shop.objects.get(id=id)
    if operation == 'add':
        User.make_preferred(request.user, shop)
        return redirect('home')
    elif operation == 'remove':
        User.remove_preferred(request.user, shop)
        return redirect('favorites')

@api_view(['GET', 'PUT', 'DELETE'])
def change_disliked(request, operation, id):
    """
    add or remove shop from disliked list of shops
    """
    shop = Shop.objects.get(id=id)
    if operation == 'add':
        User.make_dislike(request.user, shop)
        return redirect('home')
    elif operation == 'remove':
        User.remove_dislike(request.user, shop)
        return redirect('home')


@api_view(['GET', 'POST'])
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
    return Response(request, 'signup.html', {'form': UserSerializer(form,many=True).data})
