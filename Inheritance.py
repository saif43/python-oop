class People:
    # constructor
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def intro(self):
        print(self.id,self.name)

class Teacher(People):
    def assignedCourses(self):
        print('Physics Math')

class Student(People):
    def takenCourses(self):
        print('Programming')


saif = Student(124,'SAIF AHMED ANIK')
sajid = Teacher(234,'SAJID AHMED')

saif.intro()
saif.takenCourses()

print('------------')

sajid.intro()
sajid.assignedCourses()
