from django.db import models
from django.conf import settings

# Create your models here.

class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Product(TimestampedModel):
    ITEM_COLOR_CHOICES = [
        ('Red', 'Red'),
        ('Blue', 'Blue'),
        ('Green', 'Green'),
        ('Black', 'Black'),
        ('White', 'White'),
        ('Other', 'Other'),
    ]
    
    ITEM_SIZE_CHOICES = [
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
    ]
    
    item_name = models.CharField(max_length=255)
    new_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    seller = models.CharField(max_length=255)
    color = models.CharField(max_length=50, choices=ITEM_COLOR_CHOICES)
    size = models.CharField(max_length=10, choices=ITEM_SIZE_CHOICES)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.item_name


from django.contrib.auth.models import User

class Rating(TimestampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.FloatField(blank=True, null=True)
    

    def __str__(self):
        return f"{self.user.username} - {self.item.item_name} - {self.rating}"



