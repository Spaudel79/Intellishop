from rest_framework import serializers
from .models import Product
from django.contrib.auth import get_user_model

User = get_user_model()

class ProductSerializer(serializers.ModelSerializer):
    # created_by = serializers.ReadOnlyField(source='created_by.username')  # Show the username of the creator

    class Meta:
        model = Product
        fields = ['id', 'item_name','new_price', 'created_at','description','image','discount','seller']

    def create(self, validated_data):
        return Product.objects.create(**validated_data)
