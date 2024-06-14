class student:
    uni="UWA"
    def __init__(self,name,stid):
        self.name=name
        self.ID=stid
        self.units=[]
    def setName(self,name):
        self.name=name
    def setID(self,stid):
        self.ID=stid
    def printName(self):
        print("name is: ", self.name)
    def printID(self):
        print("id is:", self.ID)
    def setUni(self.unit):
        student.uni=unit
    def enrol(self.unit):
        self.units.append(unit)
    def printRnrolment(self):
        print("student ",self.name,' having Id,', self.ID,"is enrolled in following")
        for unit in self.units:
            unit.printUID()
class unit:
    def __init__(self,name,unitid):
        self.name=name
        self.uid=unitid
        self.student=[]
    def setName(self,name):
        self.name=name
    def setUID(self,uid):
        self.UID=uid
    def printName(self):
        print("name of Unit is: ", self.name)
    def printID(self):
        print("Unit's id is:", self.UID)
    def senrol(self,student):
        self.student.append(student)
    def printEnrolled(self):
        print("Unit is ",self.name,' having Id,', self.UID,"is enrolled in following")
        for unit in self.units:
            unit.printID()

s1=student("Chris",323423)
s2=student("Tim",323433)
u1=unit("python","CITS1401")
u2=unit("software","CITS4401")

s1.enrol(u1)
s1.enrol(u2)
u1.senrol(s1)
u2.senrol(s1)
s2.enrol(u2)
u2.senrol(s2)

u2.printEnrolled()