from django.db import models

# Create your models here.
class Make(models.Model):
    name = models.CharField(max_length=256)

    image = models.ImageField(null=True, default=None, blank=True)

    def __str__(self):
        return self.name

class Engine(models.Model):
    name = models.CharField(max_length=256)
    max_horsepower = models.IntegerField()
    max_torque = models.IntegerField()

    image = models.ImageField(null=True, default=None, blank=True)

    def __str__(self):
        return self.name

class Car(models.Model):
    name = models.CharField(max_length=256)
    make = models.ForeignKey('Make', on_delete=models.CASCADE)
    year = models.IntegerField()
    engine = models.ForeignKey('Engine', on_delete=models.CASCADE)
    mpg_city = models.IntegerField()
    mpg_highway = models.IntegerField()

    image = models.ImageField(null=True, default=None, blank=True)

    def __str__(self):
        return self.name
 

   
