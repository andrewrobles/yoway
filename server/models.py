from django.db import models


class Food(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return f'{self.name}'


class Order(models.Model):
    name = models.CharField(max_length=45)
    instructions = models.TextField(max_length=95)

    def __str__(self):
        food_orders = FoodOrder.objects.filter(order=self)
        return f'{self.name} {self.instructions}' + ' ' + ', '.join([food_order.food.__str__() for food_order in food_orders])


class FoodOrder(models.Model):
    food = models.ForeignKey('Food', on_delete=models.CASCADE)
    order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name='food_order')
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.quantity} {self.food}'