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
        total_sales += int(s.item.price)

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
    return render(request, 'admin/sales.html')

def reports(request):
    return render(request, 'admin/reports.html')