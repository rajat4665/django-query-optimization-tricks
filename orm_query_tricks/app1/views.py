from rest_framework import generics
from django.db.models import Prefetch

from .models import (Publisher, Book, Store)
from app1.serializers import StoreSerializer


class StoreList(generics.ListCreateAPIView):
    """
    This is the normal method, where django queryset will take extra db hits for all relational columns
    i have used django debug toolbar for monitoring the number of queries
    with this default query set it shows 185 databases queries which take 59.01ms time in my local
    I have used django rest_framework pagination so it return only first 20 stores data
    """
    queryset = Store.objects.all()
    serializer_class = StoreSerializer


class OptimizedStoreList(generics.ListCreateAPIView):
    """
    this is pro method, where we are using select_related and prefetch_related queryset's methods which allow us to take relational db data in a same query.
    -- for ForeignKey relationship we use select_related method
    -- for ManyToManyField relationship we use prefetch_related method
    as you guys can see i overwrite the get_queryset method and applied the select_related and prefetch_related method
    In the result my numner of database queries reduced to 5 from 185 and the computaion time reduced 2.58ms from 59.01ms
    In the big scale application these kind of optimization plays very crusical role and boost your app speed significantly
    I have used django rest_framework pagination so it return only first 20 stores data

    """
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

    def get_queryset(self):
        return Store.objects.prefetch_related(
            Prefetch(
                'books',
                queryset= Book.objects.select_related('publisher')
            )
        )
