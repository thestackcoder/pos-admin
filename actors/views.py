from django.shortcuts import render
from rest_framework import viewsets
from actors.models import Customer,User
from actors.serializers import CustomerSerializer,UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status
from rest_framework.decorators import action
from rest_framework_extensions.mixins import NestedViewSetMixin


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class UserViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = User.objects.order_by('id')
    serializer_class = UserSerializer



@api_view(['GET', 'POST'])
def login(request):
    if request.method == 'POST':
        username= request.query_params.get('username')
        password = request.query_params.get('password')
        user = User.objects.filter(username=username, password=password)

        if user.exists():
            user_data = User.objects.get(username=username)
            user_image = user_data.image.url[7:]
            return Response({
                "status": 1, 
                "message": "User successfully logged in.",
                "data": { 
                    "id": user_data.id,        
                    "name": user_data.name,
                    "username": user_data.username,
                    "contact": user_data.contact,
                    "image": user_image
                }
            })
        else:
            return Response({
                "status": 2,
                "message": "Invalid Username or Password",
                })
        
    return Response({"message": "User Not Logged in"})


