from django.shortcuts import render
from actors.models import User
from items.models import Item
from orders.models import Order,Order_detail,Order_item
from orders.serializers import Order_detailSeriaizer,Order_itemSeriaizer,OrderSeriaizer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework_extensions.mixins import NestedViewSetMixin
from django.db.models import Avg, Max, Min
from datetime import datetime, timedelta
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

class OrderViewSet(NestedViewSetMixin,viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('-datetime')
    serializer_class = OrderSeriaizer

    # def createOrder():
    #     myStockList1 = []
    #     myStockList2 = []
    #     mySoldList1 = []
    #     mySoldList2 = []
    #     stockItems = Item.objects.all()
    #     for data in stockItems:
    #         # print("Stock =", data.name,data.stock)
    #         myStockList1.append(data.name)
    #         myStockList2.append(data.stock)
    #     stockDictionary = dict(zip(myStockList1, myStockList2))
    #     # print("Stock items ",stockDictionary)
    #     orderData = Order.objects.last()
    #     # print(orderData)
    #     orderItem = Order_item.objects.filter(order=orderData)
    #     for items in orderItem:
    #         # print(items.item.name,items.quantity)
    #         mySoldList1.append(items.item.name)
    #         mySoldList2.append(items.quantity)
    #     soldDictionary = dict(zip(mySoldList1, mySoldList2))
    #     # print("Sold items ",soldDictionary)
    #     for total in stockDictionary:
    #         if total in soldDictionary:
    #             totalRemainingStock = stockDictionary[total] - soldDictionary[total]
    #             print("Remaining Items",total, "=", totalRemainingStock)
    #             # print(totalRemainingStock)
    #             Item.objects.filter(name=total).update(stock=totalRemainingStock)
    
    # createOrder()

class Order_detailViewSet(viewsets.ModelViewSet):
    queryset = Order_detail.objects.order_by('id')
    serializer_class = Order_detailSeriaizer

class Order_itemViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Order_item.objects.order_by('id')
    serializer_class = Order_itemSeriaizer    


def orders(request):
    orders = Order.objects.all()
    total_orders = Order.objects.count()
    
    avg_order_price = Order.objects.all().aggregate(Avg("order_items__item__price"))
    avg_price = round(avg_order_price.get('order_items__item__price__avg'),1)
    
    max_order_price = Order.objects.all().aggregate(Max("order_items__item__price"))
    max_price = round(max_order_price.get('order_items__item__price__max'),1)
    
    min_order_price = Order.objects.all().aggregate(Min("order_items__item__price"))
    min_price = round(min_order_price.get('order_items__item__price__min'),1)

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
            'all_orders': orders,
            'orders': total_orders,
            'avg_price': avg_price,
            'max_price': max_price,
            'min_price': min_price,
            'orders_today': orders_today,
            'orders_monthly': orders_monthly,
            # 'orders_monthly_t': orders_monthly2,
        }
        template = 'admin/order/index.html'
    else:
        context = {}
        template = 'admin/dash.html'

    return render(request, template, context)
