from django.db import models

from customers.models import Customer
from products.models import Product


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order by {self.customer}, created at {self.created_at.date()}'

    def get_price(self):
        price = 0
        for item in self.order_items.all():
            price += item.get_price()
        return price


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items', blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    total_price = models.DecimalField(decimal_places=2, max_digits=13, default=0)
    quantity = models.IntegerField(default=1)

    def save(self, *args, **kwargs):
        self.total_price = self.get_price()
        super(OrderItem, self).save(*args, **kwargs)

    def get_price(self):
        return self.product.price * self.quantity
