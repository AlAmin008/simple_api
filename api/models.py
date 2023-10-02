from django.db import models

# Create your models here.

class employeetable(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone = models.CharField(max_length=14)
    email = models.EmailField()
    joiningdate= models.DateField()
    salary = models.IntegerField()
    team = models.CharField(max_length=500)
    position = models.CharField(max_length=500)
    division = models.CharField(max_length=100)
    district = models.CharField(max_length=100)


    def __str__(self):
        return f"{self.name}, {self.salary}"