from django.db import models


class order(models.Model):
    name = models.CharField(max_length=128, unique=True)
    cellphone = models.CharField(max_length=128, unique=True)
    c1 = models.CharField(max_length=128, unique=True)
    c2 = models.CharField(max_length=128, unique=True)
    c3 = models.CharField(max_length=128, unique=True)
    c4 = models.CharField(max_length=128, unique=True)
    take = models.TextField()
    def __str__(self):
        return self.name
    