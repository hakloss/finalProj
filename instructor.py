class Instructor(Account):
    """instructor child class from Account ABC"""

    def __init__(self):
        self.role = "instructor"

    def getRole(self):
        return self.role

    def setRole(self, role):
        self.role = role
