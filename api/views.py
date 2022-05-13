from django.shortcuts import render

def index(request):
    return render(request, 'chat/index.html', {})

def guest(request):
    return render(request, 'chat/guest.html', {
        'room_name': 'orders'
    })

def host(request):
    return render(request, 'chat/host.html', {
        'room_name': 'orders'
    })
    



