# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, Client
from .models import user, course, section, lab

# Create your tests here.
class LoginList(TestCase):
    client = None
    courses = None

    def setUp(self):
        self.client = Client()
        self.courses = {"CS361":["Intro to software engineering"], "CS337":["System Programming"]}

        for i in self.courses.keys():
            temp = Client(name = i, password = i)
            temp.save()
            for j in self.courses[i]:
                Courses(name = j, owner = temp).save()

    def test_CorrectName(self):
        for i in self.courses.keys():
            resp = self.client.post("/", {"name":i, "password":i}, follow = True)
            self.assertEqual(resp.context["name"],i , "Name was not passed from the Login list")


    def test_complete(self):
        for i in self.courses.keys():
            resp = self.client.post("/", {"name":i, "password":i}, follow = True)
            for j in self.courses[i]:
                self.assertIn(resp.context["course"], i, "A course is missing, for:" + i)

    def test_noExtra(self):
        for i in self.courses.keys():
            resp = self.client.post("/",{"name":i, "password":i}, follow = True)
            for j in self.courses[i]:
                self.assertIn(j,self.courses[i], "There is one extra course, user:" + i)


class Login_success(TestCase):
    client = None
    courses = None

    def setUp(self):
        self.client = Client()
        self.client = {"CS361":["Intro to software engineering"], "CS337":["System Programming"]}

        for i in self.courses.keys():
            temp = Client(name = i, password = i)
            temp.save()
            for j in self.courses[i]
                Courses(name = j, owner = temp).save()

    def test_validLogin(self):
        resp = self.client.post("/", {"name": "one", "password":"one"}, follow = True)
        self.assertEqual(resp.status_code, 200) #Ok

class LoginFail(TestCase):
    client = None
    courses = None

    def setUp(self):
        self.client = Client()
        self.client = {"CS361": ["Intro to software engineering"], "CS337": ["System Programming"]}

        for i in self.courses.keys():
            temp = Client(name=i, password=i)
            temp.save()
            for j in self.courses[i]
                Courses(name=j, owner=temp).save()


    def test_noPassword(self):
        resp = self.client.post("/",{"name": "admin", "password": "instructor"}, follow = True)
        self.assertEqual(resp.context["message"],"bad password", "Failed login password, ,user: admin, password: instructor")
        self.assertEqual(resp.status_code, 302)

    def test_badPassword(self):
        resp = self.client.post("/",{"name": "admin", "password": "ta"}, follow = True)
        self.assertEqual(resp.context["message"],"bad password", "Failed login password, user: admin, password: ta, ta valid for another user")
        self.assertEqual(resp.status_code, 302)



class CreateAccount(TestCase):
    client = None
    courses = None

    def setUp(self):
        self.client = Client()
        response = self.client.post('/', {'name': 'newuser', 'password':'newuser'})
        self.assertEqual(response.status_code, 302)

    def accountcreated(self):
        response = self.client.post('/', {"name": "newuser", "password":"newuser"}, follow = True)
        self.assertEqual(response.context["message"], "Account successfully created", "User : " + 'newuser' + "password:" + 'newuser')
        self.assertEqual(response.status_code, 302)

    def noneforemptyfields(self):
        response = self.client.post('/', {"name": "", " ": "one"}, follow=True)
        self.assertEqual(response.context["message"], "Account not created","Need username and password")
        self.assertEqual(response.status_code, 400)

    def duplicateuser(self):
        response = self.client.post('/', {"name": "user2", "password": "newuser"}, follow=True)
        self.assertEqual(response.context["message"], "Account not created", "name: user2 already exists")
        self.assertEqual(response.status_code, 302)

class CreateCourse(TestCase):
    def setUp(self):
        self.client = Client()
        response = self.client.post('/', {'name': 'newcourse'})
        self.assertEqual(response.status_code, 302)

    def courseCreated(self):
        response = self.client.post('/', {"name": "newcourse"}, follow=True)
        self.assertEqual(response.context["message"], "Course successfully created",
                         "Course : newcourse")
        self.assertEqual(response.status_code, 302)

    def emptyCourseName(self):
        response = self.client.post('/', {"name": ""}, follow=True)
        self.assertEqual(response.context["message"], "Course not created","Needs name")
        self.assertEqual(response.status_code, 400)

    def duplicateCourse(self):
        response = self.client.post('/', {"name": "course2"}, follow=True)
        self.assertEqual(response.context["message"], "Course not created", "name: course2 already exists")
        self.assertEqual(response.status_code, 302)