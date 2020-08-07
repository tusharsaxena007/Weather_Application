from django.db import models


class city(models.Model):
    name = models.CharField(max_length =30 )
    temperature = models.FloatField(max_length= 20, default =0.00)
    image = models.CharField(max_length=100, default='')
    condition = models.CharField(max_length= 20, default ="")

    def __str__(self):
        return self.name


