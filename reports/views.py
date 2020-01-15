from django.shortcuts import render
from django.http import HttpResponse
from orders.models import Order, Order_item
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Avg, Max, Min, Sum
from datetime import datetime, timedelta,date
import requests
from actors.models import User
# from .forms import ItemReport

@staff_member_required
def get_employee_performance(request):
    e_report = request.POST.get('ereport')
    user = request.POST.get('ereportuser')
    today = date.today()
    last_week = datetime.now() - timedelta(days=8)
    last_month = datetime.now() - timedelta(days=30)  
    total_sale = 0
    cashier = ''
    if e_report == 'monthly_report':
        monthly_employee = Order_item.objects.filter(datetime__range=[last_month, today]).filter(order__user_id=user).values('order__user_id__username','item__price','quantity').order_by('item__name')
        if monthly_employee:
            total_sale = 0
            for employee in monthly_employee:
                total_sale = total_sale + (employee['quantity'] * employee['item__price'])
                cashier = employee['order__user_id__username']
        else:
            total_sale = 0
            cashier = User.objects.get(id=user)

    elif e_report == 'weekly_report':
        weekly_employee = Order_item.objects.filter(datetime__range=[last_week, today]).filter(order__user_id=user).values('order__user_id__username','item__price','quantity').order_by('item__name')
        if weekly_employee:
            total_sale = 0
            for employee in weekly_employee:
                total_sale = total_sale + (employee['quantity'] * employee['item__price'])
                cashier = employee['order__user_id__username']
        else:
            total_sale = 0
            cashier = User.objects.get(id=user)

    elif e_report == 'daily_report':
        daily_employee =Order_item.objects.filter(datetime__range=[today, today]).filter(order__user_id=user).values('order__user_id__username','item__price','quantity').order_by('item__name')  
        if daily_employee:
            total_sale = 0
            for employee in daily_employee:
                total_sale = total_sale + (employee['quantity'] * employee['item__price'])
                cashier = employee['order__user_id__username']
        else:
            total_sale = 0
            cashier = User.objects.get(id=user)

    if request.user.is_authenticated:
        context = {'total_sale':total_sale,'cashier':cashier}
        template = 'admin/employee_performance_report.html'
    else:
        context = {}
        template = 'admin/dash.html'

    return render(request, template, context)


@staff_member_required
def get_item_report(request):
    start_date = request.POST.get('start')
    end_date = request.POST.get('end')

    order_items = Order.objects.filter(datetime__date__range=[start_date, end_date])
    
    if request.user.is_authenticated:
        context = {'order_items':order_items}
        template = 'admin/output.html'
    else:
        context = {}
        template = 'admin/dash.html'
    return render(request, template, context)

@staff_member_required
def daily_sales_report(request):
    # orders = Order.items.all()
    # context = {'all_orders': orders}
    response = requests.get('http://localhost:8000/api/v1/orders/')
    print(response)
    data = response.json()
    context = {'data': data}
    print(data)
    return render(request, 'admin/reports.html', context)
    


            
