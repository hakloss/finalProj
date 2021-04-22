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
        m = request.session["name"]
        #if m doesn't have a name
        #This is account validation and should become a function
        #return redirect("/login/")

    def post(self, request):
        pass

class CreateAccount(View):
    def get(self, request):

        # if m doesn't have a name
        # This is account validation and should become a function
        # return redirect("/login/")
        return render(request, "CreateAccount.html", {"fname": XXX, "lname": XXX, "email":XXX, "password":XXX,
                                                      "role":XXX, "address":XXX, "city":XXX, "state":XXX, "zip":XXX, "pphone":XXX,
                                                      "wphone":XXX})


    def post(self, request):
        xfname = request.POST.get('fname')
        xlname = request.POST.get('lname')
        xemail = request.POST.get('email')
        xpass=request.POST.get('pass')
        xrole=request.POST.get('role')
        xaddress=request.POST.get('address')
        xcity=request.POST.get('city')
        xstate=request.POST.get('state')
        xzip=request.POST.get('zip')
        xpphone=request.POST.get('pphone')
        xwphone=request.POST.get('wphone')

        account = XXX(fname=xfname, lname=xlname,email=xemail, password=xpass, role=xrole)
        account.save()

class CreateCourse(View):
    def get(self, request):
        pass

    def post(self, request):
        pass