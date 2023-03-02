# from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

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
    done = False
    return render(request, 'chat/kitchen.html', {
        'room_name': 'orders',
        'orders': get_orders(done),
        'done': done
    })

# @login_required(login_url='/admin/')
def history(request):
    done = True
    orders = get_orders(done)
    orders.reverse()
    return render(request, 'chat/kitchen.html', {
        'room_name': 'orders',
        'orders': orders,
        'done': done
    })

def get_orders(done):
    return [{
        'id': order.id,
        'name': order.name,
        'done': order.done,
        'instructions': order.instructions,
        'foods': [{
            'name': food_order.food.name,
            'quantity': food_order.quantity
        } for food_order in order.food_order.all()]
    } for order in Order.objects.filter(done=done)]

def done(request, order_id):
    order = Order.objects.get(id=order_id)
    order.done = True
    order.save()
    return redirect('kitchen')

def not_done(request, order_id):
    order = Order.objects.get(id=order_id)
    order.done = False
    order.save()
    return redirect('history')