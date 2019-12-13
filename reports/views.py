from django.shortcuts import render
from django.http import HttpResponse
from orders.models import Order

# from .forms import ItemReport

def get_item_report(request):
    start_date = request.POST.get('start')
    end_date = request.POST.get('end')

    order_items = Order.objects.filter(datetime__range=[start_date, end_date])

    return HttpResponse(order_items)


            
