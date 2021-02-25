from django.db import models
from datetime import datetime

# Create your models here.

class Merchant(models.Model):
    name=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    photo=models.ImageField(upload_to='%y/%m/%d')
    description=models.TextField(blank=True)
    address=models.CharField(max_length=200)
    is_dotm=models.BooleanField(default=False)
    hire_date=models.DateTimeField(default=datetime.now(), blank=True)
    def _str_(self):
        return self.name
