from django.db import models

# Create your models here.


class Spicies(models.Model):
    name = models.CharField(max_length = 255)
    def __str__(self):
        return self.name

class Animals(models.Model):
    name = models.CharField(max_length = 255)
    last_time_feed =  models.TimeField(max_length = 255)
    duration_feed =  models.TimeField(max_length = 255)
    spicie = models.ForeignKey(Spicies, on_delete = models.CASCADE)
    def __str__(self):
        return self.name