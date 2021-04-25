# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class user(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    #  0 = admin   |   1 = instructor   |   2 = TA
    role = models.IntegerField()
    address = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=5)
    pphone = models.CharField(max_length=5)
    wphone = models.CharField(max_length=5)

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
