from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    mfg = models.CharField(max_length=50, default='test')
    price = models.FloatField(default=0.00)

    def __str__(self):
        return self.name
    