class Manager:
    __secret_no = 47
    def __init__(self, name,id, accountno):
        self.name = name 
        self.id = id 
        self.accountno = accountno 


class Employee(Manager):
    def __init__(self,name,id, accountno, manager_id):
        Manager.__init__(self,name,id, accountno)
        self.manager_id = manager_id

saif = Manager('SAIF',123,6846151864)
x    = Employee('X',221,5441646854,123)
y    = Employee('Y',222,5451646854,123)
z    = Employee('Z',223,5341646854,123)


print(saif._Manager__secret_no)
print(saif.__secret_no)





# class MyClass: 

# 	# Hidden member of MyClass 
# 	__hiddenVariable = 0
	
# 	# A member method that changes 
# 	# __hiddenVariable 
# 	def add(self, increment): 
# 		self.__hiddenVariable += increment 
# 		print (self.__hiddenVariable) 

# # Driver code 
# myObject = MyClass()	 
# myObject.add(2) 
# myObject.add(5) 

# # This line causes error 
# print (myObject.__hiddenVariable) 
