from django.shortcuts import render
from actors.models import User
from items.models import Item
from orders.models import (
    Order,
    Order_detail,
    Order_item,
    Custom_item,
    PoSystem,
    BalanceCheck
)
from orders.serializers import (
    Order_detailSeriaizer,
    Order_itemSeriaizer,
    OrderSeriaizer,
    Custom_itemSerializer,
    PoSystemSerializer,
    BalanceCheckSerializer
)
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework_extensions.mixins import NestedViewSetMixin
from django.db.models import Avg, Max, Min,Sum
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from datetime import datetime, timedelta, date
from django.utils import timezone
from django.http import Http404
from rest_framework import status
from django.core import serializers
from rest_framework.decorators import action
import json
# import json
# import requests

# def gettodo(request):
#     response = requests.get('https://jsonplaceholder.typicode.com/todos/1')
#     return response

# class TodoViewSet(viewsets.ViewSet):
#     def list(self, request):
#         todo = gettodo(request)
#         data = todo.json()
#         return Response(data=data)

class PosCheckAPIView(APIView):
    
    def post(self, request):
        id = request.data.get('pos_id')
        obj = PoSystem.objects.filter(pk=id)
        if obj:
            return Response({"detail": "Success!", "pos_id": id, "status": status.HTTP_200_OK})
        else:
            return Response({"detail": "POS doen not exists.", "status": status.HTTP_404_NOT_FOUND})


class BalanceCheckAPIView(APIView):
    def get_object(self, pk):
        try:
            return BalanceCheck.objects.get(pk=pk)
        except BalanceCheck.DoesNotExist:
            raise Http404
            
    def get(self, request):
        bal = BalanceCheck.objects.all()
        serializer = BalanceCheckSerializer(bal, many=True)
        return Response(serializer.data)

    def post(self,request):
        id = request.data.get('id', None)
        petty = request.data.get('petty')
        petty_cash = PoSystem.objects.filter(pk=petty)
        # data = serializers.serialize('json', petty_cash)
        # x = json.loads(data)
        # y = x[0]["fields"]["petty_cash"]

        if not id:
            serializer = BalanceCheckSerializer(data=request.data)
        else:
            bal = BalanceCheck.objects.get(id=id)
            serializer = BalanceCheckSerializer(bal, data=request.data)
        
        pet = float(request.data.get('petty_cash'))
        start = float(request.data.get('starting_b'))

        if(serializer.is_valid()):
            serializer.validated_data['ending_b'] = pet + start
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class BalanceCheckDetail(APIView):

    def get_object(self, pk):
        try:
            obj = BalanceCheck.objects.get(pk=pk)
            return obj 
        except BalanceCheck.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        bal = self.get_object(pk)
        serializer = BalanceCheckSerializer(bal)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        bal = self.get_object(pk)
        serializer = BalanceCheckSerializer(bal, data=request.data)
        # last_week = datetime.now() - timedelta(hours=2)
        # last_month = datetime.now() - timedelta(hours=30)  
        start = bal.start_time
        # print(start)
        now = datetime.now()
        # user = bal.user_id
        # today = date.today()

        # print(user)
        total_sales = 0
        ending_bal = Order_item.objects.filter(datetime__range=[start, now]).filter(order__user_id=user).values('item__price','quantity')
        print(ending_bal)
        if ending_bal:  
            for e in ending_bal:
                total_sales = total_sales + (e['quantity'] * e['item__price'])
        else:
            total_sales = 0
        
        # print(total_sales)

        # petty_i = request.data.get('petty')
        # obj = PoSystem.objects.filter(pk=petty_i)
        # petty_c = serializers.serialize('json', obj)
        # x = json.loads(petty_c)
        # y = x[0]["fields"]["petty_cash"]
        y = float(request.data.get('petty_cash'))
        x = float(request.data.get('starting_b'))


        if serializer.is_valid():
            serializer.validated_data['end_time'] = timezone.now()
            serializer.validated_data['ending_b'] = y + float(total_sales) + x
            serializer.validated_data['earnings'] = total_sales
            total_sales = 0
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class PosSystems(viewsets.ModelViewSet):
    queryset = PoSystem.objects.all()
    serializer_class = PoSystemSerializer

class OrderViewSet(NestedViewSetMixin,viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('-datetime')
    serializer_class = OrderSeriaizer

@api_view()
def updateStock(self):
    items_count = Order_item.objects.values('item__name').annotate(Sum('quantity')).order_by('item__name')
    myStockList1 = []
    myStockList2 = []
    mySoldList1 = []
    mySoldList2 = []
    stockItems = Item.objects.all().order_by('name')
    for data in stockItems:
        myStockList1.append(data.name)
        myStockList2.append(data.stock)
    stockDictionary = dict(zip(myStockList1, myStockList2))
    # print("Stock items ",stockDictionary)
    orderData = Order.objects.last()
    # print(orderData)
    orderItem = Order_item.objects.filter(order=orderData)
    for items in orderItem:
        # print(items.item.name,items.quantity)
        mySoldList1.append(items.item.name)
        mySoldList2.append(items.quantity)
    soldDictionary = dict(zip(mySoldList1, mySoldList2))
    for total in stockDictionary:
        if total in soldDictionary:
            totalRemainingStock = stockDictionary[total] - soldDictionary[total]
            # print("Remaining Items",total, "=", totalRemainingStock)
            Item.objects.filter(name=total).update(stock=totalRemainingStock)

    return Response({})

class Order_detailViewSet(viewsets.ModelViewSet):
    queryset = Order_detail.objects.order_by('id')
    serializer_class = Order_detailSeriaizer

class Order_itemViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Order_item.objects.order_by('id')
    serializer_class = Order_itemSeriaizer

class Custom_itemViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Custom_item.objects.order_by('id')
    serializer_class = Custom_itemSerializer


def orders(request):
    orders = Order.objects.all()
    total_orders = Order.objects.count()
    
    avg_order_price = Order.objects.aggregate(Avg("order_items__item__price"))
    avg_price = avg_order_price.get('order_items__item__price__avg')
    new_avg_price = float(0)
    if avg_price:
        new_avg_price = avg_price
    else:
        new_avg_price = float(0)
        
    max_order_price = Order.objects.aggregate(Max("order_items__item__price"))
    max_price = max_order_price.get('order_items__item__price__max')
    new_max_price = float(0)
    if avg_price:
        new_max_price = max_price
    else:
        new_max_price = float(0)

    min_order_price = Order.objects.aggregate(Min("order_items__item__price"))
    min_price = min_order_price.get('order_items__item__price__min')
    new_min_price = float(0)
    if avg_price:
        new_min_price = min_price
    else:
        new_min_price = float(0)
        
    # last week order graph 
    # today = date.today()
    # print(today)
    today = date.today()
    to_day=today.weekday()
    d6 = datetime.now() - timedelta(days=6)
    d__6 = d6.weekday()
    d6= d6.date()
    d5 = datetime.now() - timedelta(days=5)
    d__5 = d5.weekday()
    d5= d5.date()
    d4 = datetime.now() - timedelta(days=4)
    d__4 = d4.weekday()
    d4= d4.date()
    d3 = datetime.now() - timedelta(days=3)
    d__3 = d3.weekday()
    d3= d3.date()
    d2 = datetime.now() - timedelta(days=2)
    d__2 = d2.weekday()
    d2= d2.date()
    d1 = datetime.now() - timedelta(days=1)
    d__1 = d1.weekday()
    d1= d1.date()
    d0 = datetime.now() - timedelta(days=0)
    d0= d0.date()
    orders_0 = Order.objects.filter(datetime__date = d0).count()
    orders_1 = Order.objects.filter(datetime__date = d1).count()
    orders_2 = Order.objects.filter(datetime__date = d2).count()
    orders_3 = Order.objects.filter(datetime__date = d3).count()
    orders_4 = Order.objects.filter(datetime__date = d4).count()
    orders_5 = Order.objects.filter(datetime__date = d5).count()
    orders_6 = Order.objects.filter(datetime__date = d6).count()

    #orders taken in last 24 hours    
    date_from = datetime.now() - timedelta(days=1)    
    orders_today = Order.objects.filter(
        datetime__gte = date_from
    ).count()

    #orders taken in last month    
    date_from_t = datetime.now() - timedelta(days=1)    
    orders_monthly = Order.objects.filter(
        datetime__gte = date_from_t
    ).count()

    #orders taken in second last month
    # date_from_tt = datetime.today() - timedelta(days=60)
    # orders_monthly2 = Order.objects.filter(
    #     datetime__gte = date_from_tt
    # ).count()


    if request.user.is_authenticated:
        context = {
            'd__6':d__6,
            'd__5':d__5,
            'd__4':d__4,
            'd__3':d__3,
            'd__2':d__2,
            'd__1':d__1,
            'to_day':to_day,
            'orders_0':orders_0,
            'orders_1':orders_1,
            'orders_2':orders_2,
            'orders_3':orders_3,
            'orders_4':orders_4,
            'orders_5':orders_5,
            'orders_6':orders_6,
            'all_orders': orders,
            'orders': total_orders,
            'avg_price': new_avg_price,
            'max_price': new_max_price,
            'min_price': new_min_price,
            'orders_today': orders_today,
            'orders_monthly': orders_monthly,
            # 'orders_monthly_t': orders_monthly2,
        }
        template = 'admin/order/index.html'
    else:
        context = {}
        template = 'admin/dash.html'

    return render(request, template, context)
