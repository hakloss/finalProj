# -*- coding: utf-8 -*-
from instructor import Instructor
import unittest
from courses import *


class TestCourseinit(unittest.TestCase):
    def setUp(self):
        self.temp = course("Software Engineering")

    def test_name(self):
        self.assertEqual(self.temp.name, "Software Engineering")

    def test_emptySection(self):
        self.assertEqual(self.temp.sections, [])


class TestCourseaddSection(unittest.TestCase):
    def setUp(self):
        self.temp = course("Software Engineering")
        x = section(201, "MWF", "1-3")
        self.temp.addSection(x)

    def test_addSection(self):
        y = section(202, "TR", "2-10")
        self.temp.addSection(y)
        self.assertEqual(len(self.temp.sections), 2)


class TestCourselistSections(unittest.TestCase):
    def setUp(self):
        self.temp = course("Software Engineering")
        x = section(201, "MWF", "1-3")
        y = section(202, "TR", "2-10")
        z = section(203, "T", "1-2")
        self.temp.addSection(x)
        self.temp.addSection(y)
        self.temp.addSection(z)

    def test_listSection(self):
        self.assertEqual(self.temp.listSections(), ["201, MWF, 1-3", "202, TR, 2-10", "203, T, 1-2"])


class TestSectionInit(unittest.TestCase):
    def setUp(self):
        self.temp = section(201, "MWF", "1-2")

    def test_number(self):
        self.assertEqual(self.temp.number, "201")

    def test_days(self):
        self.assertEqual(self.temp.days, "MWF")

    def test_time(self):
        self.assertEqual(self.temp.time, "1-2")

    def test_emptyLabs(self):
        self.assertEqual(self.temp.labs, [])


class TestSectionGetNumber(unittest.TestCase):
    def test_getNumber(self):
        a = section(201, "MWF", "1-2")
        self.assertEqual(a.getNumber(), "201")


class TestSectionGetSchedule(unittest.TestCase):
    def test_getNumber(self):
        a = section(201, "MWF", "1-2")
        self.assertEqual(a.getSchedule(), "MWF, 1-2")


class TestSectionAddLab(unittest.TestCase):
    def setUp(self):
        self.temp = section(201, "MWF", "1-3")
        x = lab(1, "R", "1-3")
        self.temp.addLab(x)

    def test_addLab(self):
        y = lab(202, "TR", "2-10")
        self.temp.addLab(y)
        self.assertEqual(len(self.temp.labs), 2)


class TestSectionListLabs(unittest.TestCase):
    def setUp(self):
        self.temp = section(201, "MWF", "1-3")
        x = lab(1, "W", "1-3")
        y = lab(2, "TR", "2-3")
        z = lab(3, "T", "1-2")
        self.temp.addLab(x)
        self.temp.addLab(y)
        self.temp.addLab(z)

    def test_listSection(self):
        self.assertEqual(self.temp.listLabs(), ["1, W, 1-3", "2, TR, 2-3", "3, T, 1-2"])


class TestLabInit(unittest.TestCase):
    def setUp(self):
        self.temp = section(201, "MWF", "1-2")

    def test_number(self):
        self.assertEqual(self.temp.number, "201")

    def test_days(self):
        self.assertEqual(self.temp.days, "MWF")

    def test_time(self):
        self.assertEqual(self.temp.time, "1-2")


class TestLabGetNumber(unittest.TestCase):
    def test_getNumber(self):
        a = section(201, "MWF", "1-2")
        self.assertEqual(a.getNumber(), "201")


class TestLabGetSchedcle(unittest.TestCase):
    def test_getNumber(self):
        a = section(201, "MWF", "1-2")
        self.assertEqual(a.getSchedule(), "MWF, 1-2")


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
