from django.contrib import admin

from .models import Food, Order, FoodOrder

admin.site.register(Food)
admin.site.register(Order)
admin.site.register(FoodOrder)

