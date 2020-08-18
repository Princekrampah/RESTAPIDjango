from django.db import models

# Create your models here.


class Occupation(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Employee(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    salary = models.IntegerField()
    occupation = models.ManyToManyField(Occupation)


    def __str__(self):
        return self.firstName 
