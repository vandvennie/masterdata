class Person:
    __age=None
    __name=None

    def __init__(self, age, name) -> None:
        self.__name = name
        self.__age = age

    def sayHello(self):
        print("My name is {}. I am {} years old".format(self.__name, self.__age))

    def getName(self):
        return self.__name
    
    def SetName(self, newName):
        self.__name = newName

    def getAge(self):
        return self.__age
    
    def setAge(self, newAge):
        if (newAge >= 19 and newAge <= 20):
            self.__age = newAge


        


class Student(Person):

    def __init__(self, age, name) -> None:
        super().__init__(age, name)
    
    def ChaoZuoYe(self, anotherPerson: str):
        print("我是{},我抄了{}的作业".format(self.getName(), anotherPerson))
    
    

Veronica = Student(19, "V")
print(Veronica.getName())

print(Veronica.getAge())
print(Veronica.setAge(20))
print(Veronica.getAge())
Tom = Student(40, "Tom")
Tom.ChaoZuoYe(Veronica.getName())

