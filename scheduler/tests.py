# -*- coding: utf-8 -*-
import unittest
from courses import*



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