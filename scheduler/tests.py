from django.test import TestCase, Client

# Create your tests here.
class Login(TestCase):
    def setUp(self):
        self.client = Client()

    def test_validLogin(self):
        pass

    def test_invalidLogin(self):
        pass

class CreateAccount(TestCase):
    def setUp(self):
        self.client = Client()

    def accountcreated(self):
        pass

    def noneforemptyfields(self):
        pass


