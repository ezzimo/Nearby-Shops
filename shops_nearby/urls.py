from django.conf.urls import url
from django.urls import path
from shops_nearby import views

urlpatterns =[
    path('', views.home, name ='home'),
    path('FavoritShops/', views.favorites, name='favorites'),
    path('signup/', views.signup, name='signup'),
    path('connect/(?P<operation>.+)/(?P<id>\d+)/', views.change_preferred, name='change_preferred')
]
