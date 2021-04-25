# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.views import View
from scheduler.models import user, course, section, lab

# Create your views here.


# Create your views here.
class Login(View):
    def get(self, request):
        return render(request,"home.html",{"user":user.email,"password":user.password})
        #return render(request, "login.html")

    def post(self, request):
        # noSuchUser = False
        # badPassword = False
        # try:
        #     m = user.objects.get(name=request.POST['name'])
        #     badPassword = (m.password != request.POST['password'])
        # except:
        #     noSuchUser = True
        # if noSuchUser:
        #     return render(request,"home.html",{"invalidmsg":"User does not exist"})
        # elif badPassword:
        #     return render(request,"home.html",{"invalidmsg":"Please enter valid password"})
        # else:
        #     request.session["name"] = m.name
        #     return redirect("/home/")
        return render(request, "login.html")

class Home(View):
    def get(self, request):
        #m = request.session["name"]
        #if m doesn't have a name
        #This is account validation and should become a function
        #return redirect("/login/")
        return render(request,"home.html")
    def post(self, request):
        return render(request,"home.html")

class CreateAccount(View):
    def get(self, request):

        # if m doesn't have a name
        # This is account validation and should become a function
        # return redirect("/login/")

        # return render(request, "CreateAccount.html", {"fname": user.fname, "lname": user.lname, "email":user.email, "password":user.password,
        #                                               "role":user.role, "address":user.address, "city":user.city, "state":user.state,
        #                                               "zip":user.zip, "pphone":user.pphone,"wphone":user.wphone})

        return render(request, "CreateAccount.html")

    def post(self, request):
        xfname = request.POST.get('fname')
        xlname = request.POST.get('lname')
        xemail = request.POST.get('email')
        xpassword=request.POST.get('pass')
        xrole=request.POST.get('role')
        xaddress=request.POST.get('address')
        xcity=request.POST.get('city')
        xstate=request.POST.get('state')
        xzip=request.POST.get('zip')
        xpphone=request.POST.get('pphone')
        xwphone=request.POST.get('wphone')

        account = user(fname=xfname, lname=xlname,email=xemail, password=xpassword, role=xrole,
                       address=xaddress,city=xcity, state=xstate,zip=xzip,pphone=xpphone, wphone=xwphone)
        account.save()

        return render(request, "CreateAccount.html", {"successmsg": "Account has been created"})
        #return render(request, "CreateAccount.html")
class CreateCourse(View):
    def get(self, request):
        return render(request, "CreateCourse.html")

    def post(self, request):
        return render(request, "CreateCourse.html")