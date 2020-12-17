from django.db import models

# Create your models here.


class Commoninfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    date = models.DateField()
  # iska table nahi banana hai

    class Meta:
        abstract = True


class Student(Commoninfo):
    fees = models.IntegerField()
    date = None  # nahi chahiye to none kar dene ka


class Teacher(Commoninfo):
    salary = models.IntegerField()


class Contractors(Commoninfo):
    date = models.DateTimeField()  # override kar sakte hai
    salary = models.IntegerField()
