from django.shortcuts import render
from rest_framework import viewsets
from items.models import Category,Item,Favourite
from items.serializers import CategorySerializer,ItemSerializer,FavouriteSerializer,FavouriteItemSerializer
from rest_framework_extensions.mixins import NestedViewSetMixin
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import action

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



