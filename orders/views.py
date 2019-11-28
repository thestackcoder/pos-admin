from django.shortcuts import render
from actors.models import User,Customer
from items.models import Item
from orders.models import Order,Order_detail,Order_item
from orders.serializers import Order_detailSeriaizer,Order_itemSeriaizer,OrderSeriaizer
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework_extensions.mixins import NestedViewSetMixin
import json
import requests

# def gettodo(request):
#     response = requests.get('https://jsonplaceholder.typicode.com/todos/1')
#     return response

class OrderViewSet(NestedViewSetMixin,viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSeriaizer

class Order_detailViewSet(viewsets.ModelViewSet):
    queryset = Order_detail.objects.order_by('id')
    serializer_class = Order_detailSeriaizer

class Order_itemViewSet(NestedViewSetMixin,viewsets.ModelViewSet):
    queryset = Order_item.objects.order_by('id')
    serializer_class = Order_itemSeriaizer

# class TodoViewSet(viewsets.ViewSet):
#     def list(self, request):
#         todo = gettodo(request)
#         data = todo.json()
#         return Response(data=data)


