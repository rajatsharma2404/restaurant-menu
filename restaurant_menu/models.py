from django.db import models
from django.contrib.auth.models import User

MEAL_TYPE = (
    ("starters","Starters"),
    ("salads","Salads"),
    ("main_dishes","Main Dishes"),
    ("desserts","Desserts")

)

STATUS = (
    (1,"Available"),
    (0,"Unavailable")
)

# Create your models here.
class Item(models.Model):
    meal = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    meal_type = models.CharField(choices=MEAL_TYPE, max_length=200)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.IntegerField(choices=STATUS, default=1)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.meal


