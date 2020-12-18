# model inheritance in django works almost identically to the way normal class inheritance works in python.
# the base class should inherit from django.db.models.Model

# 1.abstract base classes
# 2.multi-table inheritance
# 3.proxy-model inheritance


# 1. abstract base class

# tin model banate hai...agar 3 me same fields hai kuch to 3 bar fields banane ki bajah aap ek me fields banaye aur baki 2 usko inherit kare.

# you write your base class and put abstract = true in the meta class

# this model will not be used to create any databases table.instead, when it is used as a base class for other models, its fields should will be automatically added to the child class.

# hyach object banat nai,databases madhe table nai banat nai kai nai ani directly save pn nai karta yet

# fields written in abstract base class can be overridden with another field or value, or be removed with None.

# from django.db import models

# Create your models here.


# class Commoninfo(models.Model):
#     name = models.CharField(max_length=100)
#     age = models.IntegerField()
#     date = models.DateField()
#   # iska table nahi banana hai

#     class Meta:
#         abstract = True


# class Student(Commoninfo):
#     fees = models.IntegerField()
#     date = None  # nahi chahiye to none kar dene ka


# class Teacher(Commoninfo):
#     salary = models.IntegerField()


# class Contractors(Commoninfo):
#     date = models.DateTimeField()  # override kar sakte hai
#     salary = models.IntegerField()


# multi-table inheritance

# in this inheritance, each model jave their own database  table.whih meansbase class and child class will have their  own table.

# the inheritance relationship introduces links between child  model and each of its parents(via automatically created OneToOneField).


# from django.db import models

# # Create your models here.


# class Examcenter(models.Model):
#     cname = models.CharField(max_length=100)
#     city = models.CharField(max_length=100)

#     def __str__(self):
#         return f"{self.city}"


# class Student(Examcenter):
#     name = models.CharField(max_length=100)
#     roll = models.IntegerField()

#     def __str__(self):
#         return f"{self.name}"


# class Facility(Examcenter):
#     name = models.CharField(max_length=100)
#     salary = models.IntegerField()

#     def __str__(self):
#         return f"{self.name}"


# proxy models:

# when we want to change the python behavior of a model - perhaps to  change the default manager
# , or to add the new method

# this is for what proxy model inherirtance is for:
# creating a proxy for the original model.you can creat, delete and update instance of the proxy model and all the data will be save as if you were using the original model.

# the diffrerence is that you xan change things like the default model ordering or the default manager in the proxy,without having to alter the original.


# from django.db import models

# # Create your models here.


# class Examcenter(models.Model):
#     cname = models.CharField(max_length=100)
#     city = models.CharField(max_length=100)


# class Myexamcenter(Examcenter):
#     class Meta:
#         proxy = True
#         ordering = ['id']
