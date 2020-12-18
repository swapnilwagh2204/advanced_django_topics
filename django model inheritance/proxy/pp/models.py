from django.db import models

# Create your models here.


class Examcenter(models.Model):
    cname = models.CharField(max_length=100)
    city = models.CharField(max_length=100)


class Myexamcenter(Examcenter):
    class Meta:
        proxy = True
        ordering = ['id']
