from django.db import models

class Order(models.Model):
    name = models.CharField(max_length=45)
    instructions = models.TextField(max_length=95)

    def __str__(self):
        return f'name={self.name} instructions={self.instructions}'