from django.db import models
from django.utils import timezone

# Create your models here.
from django.db import models

class FoodItem(models.Model):
    name = models.CharField(max_length=200)
    expiry_date = models.CharField(max_length=100)
    image = models.ImageField(upload_to='food_images/')


    def __str__(self):
        return self.name
    
class FoodItemPurchase(models.Model):
    MONTH_CHOICES = [
        (1, "January"), (2, "February"), (3, "March"), (4, "April"),
        (5, "May"), (6, "June"), (7, "July"), (8, "August"),
        (9, "September"), (10, "October"), (11, "November"), (12, "December")
    ]

    