from django.db import models

# Create your models here.
class Amount(models.Model):
    id = models.AutoField(primary_key=True)
    amount = models.FloatField()
