from django.contrib.gis.db import models
from django.contrib.auth.models import User

# Create your models here.
class User(models.Model):
    user = models.OneToOneField(User)
    mobile = models.CharField(max_length=20)

class Toilet(models.Model):
    TYPE_WESTERN = 'W'
    TYPE_INDIAN = 'I'

    TYPE_CHOICES = (
            (TYPE_WESTERN, 'Western'),
            (TYPE_INDIAN, 'Indian')
            )

    type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    running_water = models.BooleanField(default=False)
    well_lit = models.BooleanField(default=False)
    rating = models.IntegerField()
    comments = models.CharField(max_length=255)
    location = models.PointField()
    timestamp = models.DateTimeField(auto_now_add=True)

