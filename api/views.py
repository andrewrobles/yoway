from django.shortcuts import render

def index(request):
    return render(request, 'chat/index.html', {})

def guest(request):
    return render(request, 'chat/guest.html', {
        'room_name': 'orders'
    })

def cook(request):
    return render(request, 'chat/cook.html', {
        'room_name': 'orders'
    })
    



