class student:
    def __init__(self,name,sid):
        self.name=name
        self.ID=sid
    def setName(self,name):
        self.name=name
    def setName(self,sid):
        self.ID=sid
    def printName(self):
        print("name is: ", self.name)
    def printID(self):
        print("id is:", self.ID)

s1=student("Anna",12123)
s2=student("Tadd",12113)
s1.printID()