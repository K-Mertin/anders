from rest_framework import serializers
from inventory.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('productCode', 'productName', 'productDesc')

class ProductViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('__all__')