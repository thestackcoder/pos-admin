from django.contrib import admin
from .models import Customer,User
<<<<<<< HEAD

admin.site.register(Customer)

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'name', 'is_staff')
    list_filter = ('is_active',)

=======
# admin.site.register(Customer)
# admin.site.register(User)
class CustomerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Customer, CustomerAdmin)
class UserAdmin(admin.ModelAdmin):
    pass
>>>>>>> 2ecf0a95c0e966e5e85f2fc7ceeedb690ee54a4b
admin.site.register(User, UserAdmin)