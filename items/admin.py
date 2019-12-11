from django.contrib import admin
from .models import Category,Item,Favourite

admin.site.register(Category)

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image','category')
    list_filter = ('name',)

admin.site.register(Item, ItemAdmin)
admin.site.register(Favourite)
