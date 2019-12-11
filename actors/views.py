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
from django.db.models import Avg, Max, Min
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


def users(request):
    users = User.objects.all()
    customers = Customer.objects.all()
    total_users = User.objects.count()
    total_customers = Customer.objects.count()

    #orders taken in second last month
    # date_from_tt = datetime.today() - timedelta(days=60)
    # orders_monthly2 = User.objects.filter(
    #     datetime__gte = date_from_tt
    # ).count()


    if request.user.is_authenticated:
        context = {
            'total_users': total_users,
            'total_customers': total_customers,
            'users': users,
            'customers': customers,
        }
        template = 'admin/users/index.html'
    else:
        context = {}
        template = 'admin/dash.html'

    return render(request, template, context)

