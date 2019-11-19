from rest_framework import serializers
from actors.models import User,Customer
from items.models import Item
from orders.models import Order,Order_detail,Order_item


class Order_itemSeriaizer(serializers.ModelSerializer):
    item_name = serializers.CharField(source='item.name',required=False)
    class Meta:
        model = Order_item
        fields = ['id','item','item_name','quantity']


class OrderSeriaizer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user_id.name',required=False)
    order_items = Order_itemSeriaizer(many=True)
    class Meta:
        model = Order
        fields = ['id', 'datetime','user_id','user_name','payment_method','order_items']

    def create(self, validated_data):
        order_items = validated_data.pop('order_items')
        order = Order.objects.create(**validated_data)
        for order_item in order_items:
            Order_item.objects.create(order=order, **order_item)
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