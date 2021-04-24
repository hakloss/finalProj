# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class XXX(models.Model):
    pass

class user(models.Model):
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    #  0 = admin   |   1 = instructor   |   2 = TA
    role = models.IntegerField()
    email = models.CharField(max_length=30)
    address = models.CharField(max_length=40)

class course(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class section(models.Model):
    number = models.IntegerField()
    lectureTime = models.CharField(max_length=30)
    course = models.ForeignKey(course, on_delete=models.CASCADE)

    def __str__(self):
        return self.number

class lab(models.Model):
    number = models.IntegerField()
    labTime = models.CharField(max_length=30)
    section = models.ForeignKey(section, on_delete=models.CASCADE)

    def __str__(self):
        return self.number

