from django.db import models
from users.models import CustomUser


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return self.name
    
class Cart(models.Model):
    user = models.ForeignKey(CustomUser, related_name='carts', on_delete=models.CASCADE)
    selected_products = models.ManyToManyField('Product', related_name='carts')

    def __str__(self):
        return f"Cart for {self.user.user.username}"