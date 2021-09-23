from django.db import models

# Create your models here.
class TableI(models.Model):
    name = models.CharField("name", max_length=100, primary_key=True)
    birth = models.DateField("birth")
    height = models.FloatField("height")
