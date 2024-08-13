from django.db import models
from django.contrib.auth.models import User

MEAL_KINDS = (
    ("starters", "Starters"),
    ("salads", "Salads"),
    ("main_dishes", "Main Dishes"),
    ("deserts", "Deserts"),
)

AVAILABILITY = (
    (0, "Unavailable"),
    (1, "Available"),
)


class Meal(models.Model):
    name = models.CharField(max_length=1500, unique=True)
    description = models.CharField(max_length=5000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100, choices=MEAL_KINDS)
    status = models.IntegerField(max_length=10, choices=AVAILABILITY, default=1)
    cook = models.ForeignKey(User, on_delete=models.PROTECT)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)