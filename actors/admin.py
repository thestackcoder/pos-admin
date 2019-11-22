from django.contrib import admin
from .models import Customer,User
# admin.site.register(Customer)
# admin.site.register(User)
class CustomerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Customer, CustomerAdmin)
class UserAdmin(admin.ModelAdmin):
    pass
admin.site.register(User, UserAdmin)