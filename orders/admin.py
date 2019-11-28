from django.contrib import admin
from .models import Order
from django.contrib.auth.models import Group

class OrderAdmin(admin.ModelAdmin):
    # list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['datetime']
    # search_fields = ['customer']


admin.site.register(Order, OrderAdmin)
admin.site.unregister(Group)
