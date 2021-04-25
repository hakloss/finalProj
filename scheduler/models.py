# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class user(models.Model):
    fname = models.CharField(max_length=30, default='empty')
    lname = models.CharField(max_length=30, default='empty')
    email = models.CharField(max_length=30, default='empty')
    password = models.CharField(max_length=30, default='empty')
    #  0 = admin   |   1 = instructor   |   2 = TA
    #role = models.IntegerField()
    address = models.CharField(max_length=40, default='empty')
    city = models.CharField(max_length=40, default='empty')
    #state = models.CharField(max_length=2)
    zip = models.CharField(max_length=5, default='empty')
    pphone = models.CharField(max_length=5, default='empty')
    wphone = models.CharField(max_length=5, default='empty')

    def __str__(self):
        return self.user_text

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
