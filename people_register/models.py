from django.db import models


# Create your models here.

class Position(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class People(models.Model):
    objects = None
    Email = models.CharField(max_length=100)
    Students = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    Father_name = models.CharField(max_length=100)
    Father_occ = models.CharField(max_length=100)
    Address = models.CharField(max_length=500)
    College = models.ForeignKey(Position, on_delete=models.CASCADE)
