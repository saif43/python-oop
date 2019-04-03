class Student():
    # constructor
    def __init__(self, name, age, cell):
        self.name = name
        self.age = age
        self.cell = cell

saif = Student('Saif',24,'01674339903')
Titu = Student('Titu',34,'01974339903')

print(saif.name,saif.cell,saif.age)
print(Titu.name,Titu.cell,Titu.age)


