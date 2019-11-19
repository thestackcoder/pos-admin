from django.db import models
from actors.models import Customer,User
from items.models import Item

class Order(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    #customer_id = models.ForeignKey(Customer, on_delete = models.CASCADE,)
    user_id = models.ForeignKey(User, on_delete = models.CASCADE,)
    payment_method = models.CharField(max_length=50,null=True)
    # order_item_id = models.ForeignKey(Order_item, related_name='order', on_delete = models.CASCADE,)

class Order_item(models.Model):
    item = models.ForeignKey(Item, on_delete = models.CASCADE,)
    quantity = models.IntegerField(null=True)
    order = models.ForeignKey(Order, related_name='order_items', on_delete=models.CASCADE)

    class Meta:
        unique_together = ['item', 'order']

class Order_detail(models.Model):
    order_item_id = models.ForeignKey(Order_item, on_delete = models.CASCADE,)
    order_id = models.ForeignKey(Order, related_name='order', on_delete = models.CASCADE,)
