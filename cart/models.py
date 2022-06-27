from django.db import models
from ShopApp.models import products


# Create your models here.


class cart(models.Model):
    def __str__(self):
        return self.cart_id

    cart_id = models.CharField(max_length=150, unique=True)


class ct_items(models.Model):
    product = models.ForeignKey(products, on_delete=models.CASCADE)
    items = models.ForeignKey(cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.product

    def total(self):
        return self.product.p_price*self.quantity
