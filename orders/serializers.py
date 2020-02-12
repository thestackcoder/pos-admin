from rest_framework import serializers
from actors.models import User,Customer
from items.models import Item
from orders.models import (
    Order,
    Order_detail,
    Order_item,
    Custom_item,
    PoSystem,
    BalanceCheck
)
from django.db.models import Avg, Max, Min,Sum
from rest_framework.response import Response

class Custom_itemSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Custom_item
        fields = ['id', 'amount', 'user_id']

class Order_itemSeriaizer(serializers.ModelSerializer):
    item_name = serializers.CharField(source='item.name',required=False)
    item_price = serializers.CharField(source='item.price',required=False)

    class Meta: 
        model = Order_item
        fields = ['id','item','item_name', 'item_price', 'quantity']


class OrderSeriaizer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user_id.name',required=False)
    customer_name = serializers.CharField(source='customer.name',required=False)
    datetime = serializers.DateTimeField(format="%b %d, %Y %H:%M %p", read_only=True)
    order_items = Order_itemSeriaizer(many=True)
    custom_items = Custom_itemSerializer(many=True)

    class Meta: 
        model = Order
        fields = ['id', 'datetime','user_id', 'user_name', 'customer', 'customer_name', 'payment_method', 'order_items', 'custom_items']

    def create(self, validated_data):
        order_items = validated_data.pop('order_items')
        custom_items = validated_data.pop('custom_items')
        order = Order.objects.create(**validated_data)
        for order_item in order_items:
            Order_item.objects.create(order=order, **order_item)
        for custom_item in custom_items:
            Custom_item.objects.create(order=order, **custom_item)
        # updateStock()
        return order


    def update(self, instance, validated_data):
        order_items = validated_data.pop('order_items')
        orders_data = (instance.order_items).all()
        orders_data = list(orders_data)
        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.payment_method = validated_data.get('payment_method', instance.payment_method)
        instance.save()

        for order_item in order_items:
            order_data = orders_data.pop(0)
            order_data.item = order_item.get('item', order_data.item)
            order_data.quantity = order_item.get('quantity', order_data.quantity)
            order_data.save()
        return instance

class Order_detailSeriaizer(serializers.ModelSerializer):
    class Meta:
        model = Order_detail
        fields = ['id','order_id','order_item_id',]

class PoSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoSystem
        fields = ['pos_id', 'petty_cash']

class BalanceCheckSerializer(serializers.ModelSerializer):
    start_time = serializers.DateTimeField(format="%b %d, %Y %H:%M %p", required=False)
    end_time = serializers.DateTimeField(format="%b %d, %Y %H:%M %p", required=False)
    # petty_cash = serializers.FloatField(source='petty.petty_cash', required=False)

    class Meta:
        model = BalanceCheck
        fields = ['id', 'user_id', 'pos_id', 'petty_cash', 'starting_b', 'ending_b', 'earnings', 'start_time', 'end_time']


def updateStock():
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
