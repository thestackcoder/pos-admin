from django.shortcuts import render
from django.http import HttpResponse
from orders.models import Order
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.contrib.admin.views.decorators import staff_member_required
import requests
# from .forms import ItemReport

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
    


            
