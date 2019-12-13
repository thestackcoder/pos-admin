from django.shortcuts import render
from django.http import HttpResponse
from orders.models import Order
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render_to_response
# from .forms import ItemReport

def get_item_report(request):
    start_date = request.POST.get('start_date')
    end_date = request.POST.get('end_date')

    print(start_date)
    print(end_date)

    order_items = Order.objects.filter(datetime__range=[start_date, end_date])
    print(order_items)

    return HttpResponse(order_items)


            
