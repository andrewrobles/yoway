from django.db import models

class Order(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name