from django.contrib.gis.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Category(models.Model):
    category_name = models.CharField(max_length=128)

    def __str__(self):
        return self.category_name


class Request(models.Model):

    #requestor details
    requestor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='requests')
    location = models.PointField(srid=4326,geography=True)
    address = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=50, default='')
    state = models.CharField(max_length=50, default='')

    #request details
    requirement = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='requests')
    urgency_rating = models.FloatField(default=5, validators=[MinValueValidator(1), MaxValueValidator(10)])
    created = models.DateTimeField(auto_now=True)

    #remarks
    user_remarks = models.TextField(max_length=1024, blank=True)
    admin_remarks = models.TextField(max_length=1024, blank=True)

    #status
    status_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.requestor.username+str(self.created);
