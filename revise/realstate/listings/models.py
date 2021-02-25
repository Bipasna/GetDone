from django.db import models
from merchants.models import Merchant
from datetime import datetime

# Create your models here.

class Listing(models.Model):
    merchant=models.ForeignKey(Merchant, on_delete=models.DO_NOTHING)
    title=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    description=models.TextField()
    city=models.CharField(max_length=200)
    state=models.CharField(max_length=200)
    floors=models.DecimalField(max_digits=2, decimal_places=2)
    bathroom=models.IntegerField()
    garage=models.BooleanField(default=True)
    photo_main=models.ImageField(upload_to='photo%y/%m/%d',blank=True)
    road_feet=models.DecimalField(max_digits=2, decimal_places=2)

    photo_second=models.ImageField(upload_to='photo/%y/%m/%d',blank=True)
    photo_second=models.ImageField(upload_to='photo/%y/%m/%d',blank=True)
    photo_second=models.ImageField(upload_to='photo/%y/%m/%d',blank=True)
    photo_second=models.ImageField(upload_to='photo/%y/%m/%d',blank=True)
    photo_second=models.ImageField(upload_to='photo/%y/%m/%d',blank=True)
    is_published=models.BooleanField(default=True)
    published_date=models.DateTimeField(default= datetime.now)
    def _str_(self):
        return self.title

    