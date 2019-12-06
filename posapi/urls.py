from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from orders.views import orders
from items.views import items

admin.site.site_header = "Smart POS - Administration"
admin.site.site_title = "Smart POS"
admin.site.index_title = "Welcome to POS Admin Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/dashboard/', views.dashboard),
    path('admin/sales/', views.sales),
    path('admin/reports/', views.reports),
    path('admin/order/index/', orders),
    path('admin/item/index/', items),
    path('api/v1/',include('api.urls')),
    path('api-auth/',include('rest_framework.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)