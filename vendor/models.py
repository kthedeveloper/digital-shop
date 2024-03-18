from django.db import models


# Create your models here.
class GoodModel(models.Model):
    distributor = models.CharField(max_length=50, null=False)
    price = models.CharField(max_length=50, blank=True, null=True)
    data = models.CharField(max_length=65, blank=True, null=True)

    class Meta:
        db_table = 'goods'
