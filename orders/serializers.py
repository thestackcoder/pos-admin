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
import json


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
        items = order.order_items.all()
        # print(items)
        # print(items[0].item_id)
        # print(items[0].quantity)
        for item in items:
            # print(item)
            stock_obj = Item.objects.values('stock').filter(pk=item.item_id)
            stock = 0
            temp = 0
            for s in stock_obj:
                temp = s['stock']
            stock = temp
            u_stock = stock - item.quantity
            Item.objects.filter(pk=item.item_id).update(stock=u_stock)
            
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

