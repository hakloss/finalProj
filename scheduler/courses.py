class course():
    def __init__(self, name):
        self.sections = []
        self.name = name

    def addSection(self, section):
        self.sections.append(section)

    def listSections(self):
        out = []
        for sec in self.sections:
            out.append(sec.getNumber() + ", " + sec.getSchedule())
        return out

class section():
    def __init__(self, number, days, time):
        self.labs = []
        self.number = str(number)
        self.time = time
        self.days = days

    def getNumber(self):
        return self.number

    def getSchedule(self):
        return self.days + ", " + self.time

    def addLab(self, lab):
        self.labs.append(lab)

    def listLabs(self):
        out = []
        for sec in self.labs:
            out.append(sec.getNumber() + ", " + sec.getSchedule())
        return out


class lab():
    def __init__(self, number, days, time):
        self.number = str(number)
        self.time = time
        self.days = days

    def getNumber(self):
        return self.number

    def getSchedule(self):
        return self.days + ", " + self.time
