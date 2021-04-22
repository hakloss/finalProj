from scheduler.accounts.account import Account


class Instructor(Account):
    """instructor child class from Account ABC"""

    def __init__(self):
        self.role = "Instructor"
        self.name = None
        self.email = None
        self.address = None
        self.streetName = None
        self.zip = None
        self.state = None
        self.phoneNumber = None

    def setRole(self, role):
        self.role = role

    def getRole(self):
        return self.role

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setEmail(self, email):
        self.email = email

    def getEmail(self):
        return self.email

    def setAddress(self, address, streetName, zip, state):
        self.address = address
        self.streetName = streetName
        self.zip = zip
        self.state = state

    def getAddress(self):
        return self.address

    def getStreetName(self):
        return self.streetName

    def getZip(self):
        return self.zip

    def getState(self):
        return self.state

    def setPhone(self, phoneNumber):
        self.phoneNumber = phoneNumber

    def getPhone(self):
        return self.phoneNumber
