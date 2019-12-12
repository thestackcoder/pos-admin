from django.db import models
from actors.models import Customer,User
from items.models import Item
from datetime import datetime

class Order(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE,)
    user_id = models.ForeignKey(User, on_delete = models.CASCADE,)
    payment_method = models.CharField(max_length=50,null=True)
    # order_item_id = models.ForeignKey(Order_item, related_name='order', on_delete = models.CASCADE,)

    def __str__(self):
        return self.datetime.strftime("%m/%d/%Y, %H:%M:%S")
    

class Order_item(models.Model):
    item = models.ForeignKey(Item, on_delete = models.CASCADE,blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    order = models.ForeignKey(Order, related_name='order_items', on_delete=models.CASCADE,blank=True, null=True)

    class Meta:
        unique_together = ['item', 'order']

class Order_detail(models.Model):
    order_item_id = models.ForeignKey(Order_item, on_delete = models.CASCADE,)
    order_id = models.ForeignKey(Order, related_name='order', on_delete = models.CASCADE,)
