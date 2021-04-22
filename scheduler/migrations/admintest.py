from __future__ import unicode_literals
from administrator import Administrator
import unittest

class TesAdministratorInit(unittest.TestCase):
    # test creation
    def setUp(self):
        self.admin = Administrator()

    def test_default(self):
        self.assertEqual(self.admin.getRole(), "Administrator", msg="Default; role")
        self.assertEqual(self.admin.getName(), None, msg="Default; name")
        self.assertEqual(self.admin.getAddress(), None, msg="Default; address")
        self.assertEqual(self.admin.getZip(), None, msg="Default; zip code")
        self.assertEqual(self.admin.getState(), None, msg="Default; state")
        self.assertEqual(self.admin.getEmail(), None, msg="Default; email")
        self.assertEqual(self.admin.getPhone(), None, msg="Default; phone number")
        self.assertEqual(self.admin.getStreetName(), None, msg="Default; street name")



class TestRole(unittest.TestCase):
    # test role attribute
    def setUp(self):
        self.admin = Administrator()
        self.admin.setRole("Administrator")

    def test_role(self):
        self.assertEqual(self.admin.getRole(), "Administrator", msg="Good role")
        self.assertEqual(self.admin.getRole(), "TA", msg="Wrong role")


class TestName(unittest.TestCase):
    # test name attribute
    def setUp(self):
        self.admin = Administrator()
        self.admin.setName("Nyangono")

    def test_name(self):
        self.assertEqual(self.admin.getname(), "Paul", msg="name failed")
        self.assertEqual(self.admin.getName(), "Nyangono", msg="Good name")


class TestStreetName(unittest.TestCase):
    # test street name attribute
    def setUp(self):
        self.admin = Administrator()
        self.admin.setStreetName("Mboppi")

    def test_street_name(self):
        self.assertEqual(self.admin.getStreetName(), "Kenwood Boulevard", msg="Failure street name")
        self.assertEqual(self.admin.getStreetName(), "Mboppi", msg="Right street name")


class TestPhone(unittest.TestCase):
    # test phone attribute
    def setUp(self):
        self.admin = Administrator()
        self.admin.setPhone("4142294040")

    def test_phone(self):
        self.assertEqual(self.admin.getPhone(), "1334427892", msg="Failed phone number")
        self.assertEqual(self.admin.getPhone(), "4142294040", msg="Good phone number")


class TestEmail(unittest.TestCase):
    # test email attribute
    def setUp(self):
        self.admin = Administrator()
        self.admin.setEmail("bobi@gmail.py")

    def test_email(self):
        self.assertEqual(self.admin.getEmail(), "nono@p.com", msg="email failed")
        self.assertNotEqual(self.admin.getEmail(), "bobi@gmail.com", msg="Email are the same")
        self.assertEqual(self.admin.getEmail(), "bobi@gmail.com", msg="Right email")


class TestZip(unittest.TestCase):
    # test zip code attribute
    def setUp(self):
        self.admin = Administrator()
        self.admin.setZip("53211")

    def test_zip_code(self):
        self.assertEqual(self.admin.getZip(), "53211", msg="Good zip")
        self.assertNotEqual(self.admin.getZip(), "51211", msg="Good. Zip are not equal")


class TestState(unittest.TestCase):
    # test state attribute
    def setUp(self):
        self.admin = Administrator()
        self.admin.setState("Wisconsin")

    def test_state(self):
        self.assertEqual(self.admin.getState(), "Wisconsin", msg="Good state")
        self.assertEqual(self.admin.getState(), "California", msg="State Failure")


class TestAddress(unittest.TestCase):
    # test address attribute
    def setUp(self):
        self.admin = Administrator()
        self.admin.setaddress("1234")

    def test_address(self):
        self.assertEqual(self.admin.getaddress(), "1234", msg="Good address")
        self.assertEqual(self.admin.getAddress(), "2120", msg="Address failed")


