from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank = True)
    price = models.DecimalField(max_digits=6, decimal_places = 2)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer_name = models.CharField(max_length = 100)
    customer_phone = models.CharField(max_length = 13)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField(default = 1)
    order_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order by {self.customer_name} - {self.product.name}"