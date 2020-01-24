from django.shortcuts import render
from actors.models import User, Customer
from orders.models import Order, Order_item
from items.models import Item
from datetime import datetime, timedelta, date
from django.db.models import Avg, Max, Min,Sum

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

    d0 = datetime.now() - timedelta(days=0)
    d0= d0.date()
    m1 = d0.month
    m2 = m1+1
    m3 = m1+2
    m4 = m1+3
    m5 = m1+4
    m6 = m1+5
    m7 = m1+6
    m8 = m1+7
    m9 = m1+8
    m10 = m1+9
    m11 = m1+10
    m12 = m1+11
    m1_query =Order_item.objects.filter(datetime__month__range=[m1, m1]).values('item__price','quantity').annotate(Sum('item__price')).annotate(Sum('quantity')).order_by('item__name')
    m1_sale = 0
    for sale in m1_query:
        m1_sale += sale['item__price'] * sale['quantity__sum']
    m2_query =Order_item.objects.filter(datetime__month__range=[m2, m2]).values('item__price','quantity').annotate(Sum('item__price')).annotate(Sum('quantity')).order_by('item__name')
    m2_sale = 0
    for sale in m2_query:
        m2_sale += sale['item__price'] * sale['quantity__sum']
    m3_query =Order_item.objects.filter(datetime__month__range=[m3, m3]).values('item__price','quantity').annotate(Sum('item__price')).annotate(Sum('quantity')).order_by('item__name')
    m3_sale = 0
    for sale in m3_query:
        m3_sale += sale['item__price'] * sale['quantity__sum']
    m4_query =Order_item.objects.filter(datetime__month__range=[m4, m4]).values('item__price','quantity').annotate(Sum('item__price')).annotate(Sum('quantity')).order_by('item__name')
    m4_sale = 0
    for sale in m4_query:
        m4_sale += sale['item__price'] * sale['quantity__sum']
    m5_query =Order_item.objects.filter(datetime__month__range=[m5, m5]).values('item__price','quantity').annotate(Sum('item__price')).annotate(Sum('quantity')).order_by('item__name')
    m5_sale = 0
    for sale in m5_query:
        m5_sale += sale['item__price'] * sale['quantity__sum']
    m6_query =Order_item.objects.filter(datetime__month__range=[m6, m6]).values('item__price','quantity').annotate(Sum('item__price')).annotate(Sum('quantity')).order_by('item__name')
    m6_sale = 0
    for sale in m6_query:
        m6_sale += sale['item__price'] * sale['quantity__sum']
    m7_query =Order_item.objects.filter(datetime__month__range=[m7, m7]).values('item__price','quantity').annotate(Sum('item__price')).annotate(Sum('quantity')).order_by('item__name')
    m7_sale = 0
    for sale in m7_query:
        m7_sale += sale['item__price'] * sale['quantity__sum']
    m8_query =Order_item.objects.filter(datetime__month__range=[m8, m8]).values('item__price','quantity').annotate(Sum('item__price')).annotate(Sum('quantity')).order_by('item__name')
    m8_sale = 0
    for sale in m8_query:
        m8_sale += sale['item__price'] * sale['quantity__sum']
    m9_query =Order_item.objects.filter(datetime__month__range=[m9, m9]).values('item__price','quantity').annotate(Sum('item__price')).annotate(Sum('quantity')).order_by('item__name')
    m9_sale = 0
    for sale in m9_query:
        m9_sale += sale['item__price'] * sale['quantity__sum']
    m10_query =Order_item.objects.filter(datetime__month__range=[m10, m10]).values('item__price','quantity').annotate(Sum('item__price')).annotate(Sum('quantity')).order_by('item__name')
    m10_sale = 0
    for sale in m10_query:
        m10_sale += sale['item__price'] * sale['quantity__sum']
    m11_query =Order_item.objects.filter(datetime__month__range=[m11, m11]).values('item__price','quantity').annotate(Sum('item__price')).annotate(Sum('quantity')).order_by('item__name')
    m11_sale = 0
    for sale in m11_query:
        m11_sale += sale['item__price'] * sale['quantity__sum']
    m12_query =Order_item.objects.filter(datetime__month__range=[m12, m12]).values('item__price','quantity').annotate(Sum('item__price')).annotate(Sum('quantity')).order_by('item__name')
    m12_sale = 0
    for sale in m12_query:
        m12_sale += sale['item__price'] * sale['quantity__sum']

    if request.user.is_authenticated:
        template = 'admin/dashboard.html'
        context = {
            'm1_sale':m1_sale,
            'm2_sale':m2_sale,
            'm3_sale':m3_sale,
            'm4_sale':m4_sale,
            'm5_sale':m5_sale,
            'm6_sale':m6_sale,
            'm7_sale':m7_sale,
            'm8_sale':m8_sale,
            'm9_sale':m9_sale,
            'm10_sale':m10_sale,
            'm11_sale':m11_sale,
            'm12_sale':m12_sale,
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
    user_count = User.objects.count()
    total_orders = Order.objects.count()
    total_customers = Customer.objects.count()
    total_customers = Customer.objects.count()
    sales = Order_item.objects.all()
    items = Item.objects.all().order_by('name')
    today = date.today()
    last_week = datetime.now() - timedelta(days=8)
    daily_sale_query =Order_item.objects.filter(datetime__range=[today,today]).values('item__price','quantity').annotate(Sum('item__price')).annotate(Sum('quantity')).order_by('item__name')
    weekly_sale_query =Order_item.objects.filter(datetime__range=[last_week, today]).values('item__price','quantity').annotate(Sum('item__price')).annotate(Sum('quantity')).order_by('item__name')
    last_week_sale = 0
    daily_sale = 0
    for sale in daily_sale_query:
        daily_sale += sale['item__price'] * sale['quantity__sum']
    for weekly_sale in weekly_sale_query:
        last_week_sale += weekly_sale['item__price'] * weekly_sale['quantity__sum']
    d0 = datetime.now() - timedelta(days=0)
    d0= d0.date()
    m1 = d0.month
    m2 = m1+1
    m3 = m1+2
    m4 = m1+3
    m5 = m1+4
    m6 = m1+5
    m7 = m1+6
    m8 = m1+7
    m9 = m1+8
    m10 = m1+9
    m11 = m1+10
    m12 = m1+11
    m1_query =Order_item.objects.filter(datetime__month__range=[m1, m1]).values('item__price','quantity').annotate(Sum('item__price')).annotate(Sum('quantity')).order_by('item__name')
    m1_sale = 0
    for sale in m1_query:
        m1_sale += sale['item__price'] * sale['quantity__sum']
    m2_query =Order_item.objects.filter(datetime__month__range=[m2, m2]).values('item__price','quantity').annotate(Sum('item__price')).annotate(Sum('quantity')).order_by('item__name')
    m2_sale = 0
    for sale in m2_query:
        m2_sale += sale['item__price'] * sale['quantity__sum']
    m3_query =Order_item.objects.filter(datetime__month__range=[m3, m3]).values('item__price','quantity').annotate(Sum('item__price')).annotate(Sum('quantity')).order_by('item__name')
    m3_sale = 0
    for sale in m3_query:
        m3_sale += sale['item__price'] * sale['quantity__sum']
    m4_query =Order_item.objects.filter(datetime__month__range=[m4, m4]).values('item__price','quantity').annotate(Sum('item__price')).annotate(Sum('quantity')).order_by('item__name')
    m4_sale = 0
    for sale in m4_query:
        m4_sale += sale['item__price'] * sale['quantity__sum']
    m5_query =Order_item.objects.filter(datetime__month__range=[m5, m5]).values('item__price','quantity').annotate(Sum('item__price')).annotate(Sum('quantity')).order_by('item__name')
    m5_sale = 0
    for sale in m5_query:
        m5_sale += sale['item__price'] * sale['quantity__sum']
    m6_query =Order_item.objects.filter(datetime__month__range=[m6, m6]).values('item__price','quantity').annotate(Sum('item__price')).annotate(Sum('quantity')).order_by('item__name')
    m6_sale = 0
    for sale in m6_query:
        m6_sale += sale['item__price'] * sale['quantity__sum']
    m7_query =Order_item.objects.filter(datetime__month__range=[m7, m7]).values('item__price','quantity').annotate(Sum('item__price')).annotate(Sum('quantity')).order_by('item__name')
    m7_sale = 0
    for sale in m7_query:
        m7_sale += sale['item__price'] * sale['quantity__sum']
    m8_query =Order_item.objects.filter(datetime__month__range=[m8, m8]).values('item__price','quantity').annotate(Sum('item__price')).annotate(Sum('quantity')).order_by('item__name')
    m8_sale = 0
    for sale in m8_query:
        m8_sale += sale['item__price'] * sale['quantity__sum']
    m9_query =Order_item.objects.filter(datetime__month__range=[m9, m9]).values('item__price','quantity').annotate(Sum('item__price')).annotate(Sum('quantity')).order_by('item__name')
    m9_sale = 0
    for sale in m9_query:
        m9_sale += sale['item__price'] * sale['quantity__sum']
    m10_query =Order_item.objects.filter(datetime__month__range=[m10, m10]).values('item__price','quantity').annotate(Sum('item__price')).annotate(Sum('quantity')).order_by('item__name')
    m10_sale = 0
    for sale in m10_query:
        m10_sale += sale['item__price'] * sale['quantity__sum']
    m11_query =Order_item.objects.filter(datetime__month__range=[m11, m11]).values('item__price','quantity').annotate(Sum('item__price')).annotate(Sum('quantity')).order_by('item__name')
    m11_sale = 0
    for sale in m11_query:
        m11_sale += sale['item__price'] * sale['quantity__sum']
    m12_query =Order_item.objects.filter(datetime__month__range=[m12, m12]).values('item__price','quantity').annotate(Sum('item__price')).annotate(Sum('quantity')).order_by('item__name')
    m12_sale = 0
    for sale in m12_query:
        m12_sale += sale['item__price'] * sale['quantity__sum']
    if request.user.is_authenticated:
        context = {'items': items,
            'm1_sale':m1_sale,
            'm2_sale':m2_sale,
            'm3_sale':m3_sale,
            'm4_sale':m4_sale,
            'm5_sale':m5_sale,
            'm6_sale':m6_sale,
            'm7_sale':m7_sale,
            'm8_sale':m8_sale,
            'm9_sale':m9_sale,
            'm10_sale':m10_sale,
            'm11_sale':m11_sale,
            'm12_sale':m12_sale,
            'last_week_sale':last_week_sale,
            'daily_sale':daily_sale,
            'user_count': user_count,
            'order_count': total_orders,
            'customers_count': total_customers,
        
        
        }
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


