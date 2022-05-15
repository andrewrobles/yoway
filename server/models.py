from django.db import models


class Food(models.Model):
    name = models.CharField(max_length=45)


class Order(models.Model):
    name = models.CharField(max_length=45)
    description = models.TextField(default='')
    instructions = models.TextField(default='')
    done = models.BooleanField(default=False)


class FoodOrder(models.Model):
    food = models.ForeignKey('Food', on_delete=models.CASCADE)
    order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name='food_order')
    quantity = models.IntegerField()