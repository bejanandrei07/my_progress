
from django.utils import timezone
from django.db import models

# Create your models here.

class Measurements(models.Model):
    weight = models.FloatField(default=0)
    height = models.FloatField(default=0)
    age = models.IntegerField(default=0)
    biceps = models.FloatField(default=0)
    triceps = models.FloatField(default=0)
    shoulders = models.FloatField(default=0)
    chest = models.FloatField(default=0)
    waist = models.FloatField(default=0)
    hips = models.FloatField(default=0)
    thigs = models.FloatField(default=0)
    calves = models.FloatField(default=0)
    date_add = models.DateField(default= timezone.now)
    def __str__(self):
        return f"{self.weight}"

