from django.shortcuts import render
from actors.models import User, Customer
from orders.models import Order, Order_item
from items.models import Item

def dashboard(request):
    user_count = User.objects.count()
    total_orders = Order.objects.count()
    total_customers = Customer.objects.count()
    total_customers = Customer.objects.count()
    sales = Order_item.objects.all()
    items = Item.objects.all()

    total_sales = 0;
    for s in sales:
        total_sales += s.item.price

    if request.user.is_authenticated:
        template = 'admin/dashboard.html'
        context = {
            'user_count': user_count,
            'order_count': total_orders,
            'customers_count': total_customers,
            'sales': total_sales,
            'menu': items
        }
    else:
        context = {}
        template = 'admin/dash.html'
    return render(request, template, context)

def sales(request):
    items = Item.objects.all()
    if request.user.is_authenticated:
        context = {'items': items}
        template = 'admin/sales.html'
    else:
        context = {}
        template = 'admin/dash.html'

    return render(request, template, context)

def reports(request):
    all_user = User.objects.filter(is_superuser=False)
    if request.user.is_authenticated:
        context = {'all_users':all_user}
        template = 'admin/reports.html'
    else:
        context = {}
        template = 'admin/dash.html'

    return render(request, template, context)


