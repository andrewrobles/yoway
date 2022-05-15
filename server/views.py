# from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Food, Order

def index(request):
    return render(request, 'chat/index.html', {})

def order(request):
    return render(request, 'chat/order.html', {
        'room_name': 'orders',
        'foods': Food.objects.all()
    })

# @login_required(login_url='/admin/')
def kitchen(request):
    orders = Order.objects.all()
    return render(request, 'chat/kitchen.html', {
        'room_name': 'orders',
        'orders': orders
    })
