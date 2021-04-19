from abc import ABC

class account(ABC):

    @abstractmethod
    def setName(self, name):
        pass

    @abstractmethod
    def getName(self):
        pass

    @abstractmethod
    def setEmail(self, email):
        pass

    @abstractmethod
    def getEmail(self):
        pass

    @abstractmethod
    def setAddress(self, address, streetName, zip, state):
        pass

    @abstractmethod
    def getAddress(self):
        pass

    @abstractmethod
    def getStreetName(self):
        pass

    @abstractmethod
    def getZip(self):
        pass

    @abstractmethod
    def getState(self):
        pass

    @abstractmethod
    def setPhone(self, phoneNumber):
        pass

    @abstractmethod
    def getPhone(self):
        pass