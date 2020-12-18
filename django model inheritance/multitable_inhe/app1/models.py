from django.db import models

# Create your models here.


class Examcenter(models.Model):
    cname = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.city}"


class Student(Examcenter):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()

    def __str__(self):
        return f"{self.name}"


class Facility(Examcenter):
    name = models.CharField(max_length=100)
    salary = models.IntegerField()

    def __str__(self):
        return f"{self.name}"
