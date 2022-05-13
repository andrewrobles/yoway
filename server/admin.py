from django.contrib import admin

from .models import Order, Food

admin.site.register(Order)
admin.site.register(Food)
