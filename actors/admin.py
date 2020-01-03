from django.contrib import admin
from .models import Customer,User
from django.contrib.auth.admin import UserAdmin 

admin.site.register(Customer)

# class UserAdmin(admin.ModelAdmin):
#     list_display = ('username', 'email', 'name', 'is_staff')
#     list_filter = ('is_active',)

admin.site.register(User, UserAdmin)