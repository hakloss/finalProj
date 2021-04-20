# -*- coding: utf-8 -*-
from instructor import Instructor
import unittest


class TestInstructorInit(unittest.TestCase):
    # test creation
    def setUp(self):
        self.a = Instructor()

    def test_default(self):
        self.assertEqual(self.a.getRole(), "Instructor", msg="default broke; role")
        self.assertEqual(self.a.getName(), None, msg="default broke; name")
        self.assertEqual(self.a.getEmail(), None, msg="default broke; email")
        self.assertEqual(self.a.getAddress(), None, msg="default broke; address")
        self.assertEqual(self.a.getStreetName(), None, msg="default broke; street name")
        self.assertEqual(self.a.getZip(), None, msg="default broke; zip code")
        self.assertEqual(self.a.getState(), None, msg="default broke; state")
        self.assertEqual(self.a.getPhone(), None, msg="default broke; phone number")


class TestRole(unittest.TestCase):
    # test role attribute
    def setUp(self):
        self.a = Instructor()
        self.a.setRole("Administrator")

    def test_role(self):
        self.assertEqual(self.a.getRole(), "Administrator", msg="role failed")


class TestName(unittest.TestCase):
    # test name attribute
    def setUp(self):
        self.a = Instructor()
        self.a.setName("John")

    def test_name(self):
        self.assertEqual(self.a.getname(), "John", msg="name failed")


class TestEmail(unittest.TestCase):
    # test email attribute
    def setUp(self):
        self.a = Instructor()
        self.a.setEmail("foo.com")

    def test_email(self):
        self.assertEqual(self.a.getEmail(), "foo.com", msg="email failed")


class TestAddress(unittest.TestCase):
    # test address attribute
    def setUp(self):
        self.a = Instructor()
        self.a.setaddress("1234")

    def test_address(self):
        self.assertEqual(self.a.getaddress(), "1234", msg="address failed")


class TestStreetName(unittest.TestCase):
    # test street name attribute
    def setUp(self):
        self.a = Instructor()
        self.a.setStreetName("Kenwood Boulevard")

    def test_street_name(self):
        self.assertEqual(self.a.getStreetName(), "Kenwood Boulevard", msg="street name failed")


class TestZip(unittest.TestCase):
    # test zip code attribute
    def setUp(self):
        self.a = Instructor()
        self.a.setZip("54321")

    def test_zip_code(self):
        self.assertEqual(self.a.getZip(), "54321", msg="zip code failed")


class TestState(unittest.TestCase):
    # test state attribute
    def setUp(self):
        self.a = Instructor()
        self.a.setState("Wisconsin")

    def test_state(self):
        self.assertEqual(self.a.getState(), "Wisconsin", msg="state failed")


class TestPhone(unittest.TestCase):
    # test phone attribute
    def setUp(self):
        self.a = Instructor()
        self.a.setPhone("1234567890")

    def test_phone(self):
        self.assertEqual(self.a.getPhone(), "1234567890", msg="phone failed")
