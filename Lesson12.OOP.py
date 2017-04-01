class Person: #super class or parent class
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def displayPerson(self):
        print(self.name, "is", self.age, "years old.")
    def getName(self):
        print(self.name)
    def setName(self, name):
        self.name = name
    
class Student(Person): #subclass or child class
    def __init__(self, name, age, univer, grant):
        super().__init__(name, age)
        self.univer = univer
        self.grant = grant
    def displayStudent(self):
        if self.grant:
            print(self.name, "is", self.age, "years old studies at",self.univer, "and has grant")
        else:
            print(self.name, "is", self.age, "years old studies at",self.univer, "and hasn't grant")
    def setGrant(self, grant):
        self.grant = grant

    
madina = Person("Madina", 345)       
madina.displayPerson()

madina.setName("Kamila")
madina.getName()

bolat = Student("Bolat", 23, "SDU", True)
bolat.displayStudent()

bolat.setGrant(False)
bolat.displayStudent()


