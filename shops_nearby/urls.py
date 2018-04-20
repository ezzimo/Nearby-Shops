from django.conf.urls import url
from django.urls import path
from shops_nearby import views
from rest_framework import routers

urlpatterns =[
    path('', views.home, name ='home'),
    path('FavoritShops/', views.favorites, name='favorites'),
    path('DislikedSops/', views.dislikes, name='dislikes'),
    path('signup/', views.signup, name='signup'),
    path('(?P<operation>.+)/(?P<id>\d+)/', views.change_preferred, name='change_preferred'),
    path('connect/(?P<operation>.+)/(?P<id>\d+)/', views.change_disliked, name='change_disliked')
]
