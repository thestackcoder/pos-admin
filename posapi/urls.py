from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from orders.views import orders
from items.views import items, import_items
from actors.views import users
from reports.views import ( get_item_report, get_employee_performance, get_inventry_report, get_daily_report,
get_weekly_report, get_monthly_report )

admin.site.site_header = "Smart POS - Administration"
admin.site.site_title = "Smart POS"
admin.site.index_title = "Welcome to POS Admin Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/dashboard/', views.dashboard),
    path('admin/users/index/', users),
    path('admin/sales/', views.sales),
    path('admin/reports/', views.reports),
    path('admin/reports/output/', get_item_report, name="get_item_report"),
    # path('admin/reports/', daily_sales_report, name='daily_sales_report'),
    path('admin/reports/inventry_report/', get_inventry_report, name="get_inventry_report"),
    path('admin/reports/employee_performance_report/', get_employee_performance, name="get_employee_performance"),
    path('admin/reports/daily_report/', get_daily_report, name="get_daily_report"),
    path('admin/reports/weekly_report/', get_weekly_report, name="get_weekly_report"),
    path('admin/reports/monthly_report/', get_monthly_report, name="get_monthly_report"),
    path('admin/order/index/', orders),
    path('admin/item/index/', items),
    path('admin/item/index/', import_items, name="import_items"),
    path('api/v1/',include('api.urls')),
    path('api-auth/',include('rest_framework.urls')),

    # path('line_chart_json', line_chart_json,
    #     name='line_chart_json'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)