from rest_framework import serializers
from  shop.models import Category,Product,Customer,Order

class CategorySerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields='__all__'

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model= Product
        fields='__all__'

class CustomerSerializers(serializers.ModelSerializer):
    class Meta:
        model= Customer
        fields='__all__'
class OrderSerializers(serializers.ModelSerializer):
    Customer
    class Meta:
        model= Order
        
        fields = '__all__'

from django.urls import path
from . import views

