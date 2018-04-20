from rest_framework import serializers
from .models import Shop, User
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .views import *

class ShopSerializer(serializers.ModelSerializer):
    geo_field = "location"
    class Meta:
        model = Shop
        fields = ('location' ,'name', 'shop_pic')


class UserSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(format='hex_verbose')
    geo_field = "maplocation"
    class Meta:
        model = User
        fields =  '__all__'
