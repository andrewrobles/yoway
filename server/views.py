# from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Food

def index(request):
    return render(request, 'chat/index.html', {})

def order(request):
    return render(request, 'chat/order.html', {
        'room_name': 'orders',
        'foods': Food.objects.all()
    })

# @login_required(login_url='/admin/')
def kitchen(request):
    return render(request, 'chat/kitchen.html', {
        'room_name': 'orders'
    })
