# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.views import View
from .models import XXX

# Create your views here.


# Create your views here.
class Login(View):
    def get(self, request):
        return render(request,"home.html",{})

    def post(self, request):
        noSuchUser = False
        badPassword = False
        try:
            m = XXX.objects.get(name=request.POST['name'])
            badPassword = (m.password != request.POST['password'])
        except:
            noSuchUser = True
        if noSuchUser:
            return render(request,"home.html",{"message":"User does not exist"})
        elif badPassword:
            return render(request,"home.html",{"message":"Please enter valid password"})
        else:
            request.session["name"] = m.name
            return redirect("/home/")


class Home(View):
    def get(self, request):
        pass

    def post(self, request):
        pass

class CreateAccount(View):
    def get(self, request):
        pass

    def post(self, request):
        pass

class CreateCourse(View):
    def get(self, request):
        pass

    def post(self, request):
        pass