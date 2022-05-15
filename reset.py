from server.models import Order

for order in Order.objects.all():
    order.delete()