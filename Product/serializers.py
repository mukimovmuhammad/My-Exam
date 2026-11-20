from rest_framework import serializers
from .models import Product
from rest_framework.permissions import AllowAny

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'