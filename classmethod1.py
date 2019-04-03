from datetime import date

class Person:
    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age  = age

    def intro(self):
        print('Name:',self.name,'Age',self.age)

    @classmethod

    def calculateAge(cls, name, birthyear):
        return cls(name, date.today().year-birthyear)

    


anik = Person('SAIF AHMED ANIK',25)
titu = Person.calculateAge('AMRUL MOLLICK TITU',1988)

print(anik.age)
print(titu.age)
