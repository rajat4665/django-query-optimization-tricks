from rest_framework import serializers
from .models import (Publisher, Book, Store)

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        depth = 2
        fields = ['id', 'name', 'books']
