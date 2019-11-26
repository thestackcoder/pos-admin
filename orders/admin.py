from django.contrib import admin
from .models import Order
from django.contrib.auth.models import Group

admin.site.register(Order)
admin.site.unregister(Group)
