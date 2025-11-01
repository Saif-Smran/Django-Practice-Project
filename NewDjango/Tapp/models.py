from django.db import models
from django.utils import timezone

# Create your models here.

class TapVarity(models.Model):
    Tap_Type_Choices = [
        ('T1', 'Type 1'),
        ('T2', 'Type 2'),
        ('T3', 'Type 3'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='tapp/')
    date_added = models.DateTimeField(default=timezone.now)
    tap_type = models.CharField(max_length=2, choices=Tap_Type_Choices)
    description = models.TextField(default='')

    def __str__(self):
        return self.name