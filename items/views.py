from django.shortcuts import render
from rest_framework import viewsets
from items.models import Category,Item,Favourite
from items.serializers import CategorySerializer,ItemSerializer,FavouriteSerializer,FavouriteItemSerializer
from rest_framework_extensions.mixins import NestedViewSetMixin
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import action
from items.models import Item
from django.db.models import Avg, Max, Min
from datetime import datetime, timedelta
from orders.models import Order_item

class ItemViewSet(NestedViewSetMixin, viewsets.ModelViewSet):

    queryset = Item.objects.order_by('id')
    serializer_class = ItemSerializer

class CategoryViewSet(NestedViewSetMixin, viewsets.ModelViewSet):

    queryset = Category.objects.order_by('id')
    serializer_class = CategorySerializer


class FavouriteViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Favourite.objects.all()
    serializer_class = FavouriteSerializer


# @api_view(['GET', 'POST'])
# def addfav(request):
#     if request.method == 'POST':
#         user = request.query_params.get('user')
#         item = request.query_params.get('item')
#         data = Favourite.objects.filter(user=user, item=item)
#         if data.exists():
#             fav_data = Favourite.objects.get(user=user)
#             return Response({
#                 fav_data.user
#             })
#         else:
#             data.save()
#             return Response(fav_data,status=201) 



class FavouriteItemViewSet(NestedViewSetMixin,viewsets.ModelViewSet):

    queryset = Favourite.objects.order_by('id')
    serializer_class = FavouriteItemSerializer
    # @action(detail=True, methods=['post'])
    # def perform(request):
    #     data = request.query_params.get('user')
    #     return Response(data)
        # serializer = FavouriteSerializer(data=data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data,status=201)
        # return Response(serializer.erros,status=400)
            
        # user = request.query_params['user'] 
        # item = request.query_params['item'] 
        # serializer = self.request.query_params.get(user=user,item=item)
        
    
    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(user=request.query_params.get('user'), item=request.GET.get('item'))
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)

    # def get_queryset(request):
    #     data = self.request.query_params.get('user', 'item')
    #     serializer = FavouriteSerializer(data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=201)
    #     return Response(serializer.errors, status=400)

    
    # def perform_create(self, serializer):
    #     serializer.save()




def items(request):
    items = Item.objects.all()
    total_items = Item.objects.count()
    items_sold = Order_item.objects.count()

    # item_count = Order_item.objects.get()

    #orders taken in second last month
    # date_from_tt = datetime.today() - timedelta(days=60)
    # orders_monthly2 = Item.objects.filter(
    #     datetime__gte = date_from_tt
    # ).count()


    if request.user.is_authenticated:
        context = {
            'items': items,
            'total_items': total_items,
            'items_sold': items_sold,
            # 'item_count': item_count.quantity
            # 'orders_monthly_t': orders_monthly2,
        }
        template = 'admin/inventory/index.html'
    else:
        context = {}
        template = 'admin/dash.html'

    return render(request, template, context)
