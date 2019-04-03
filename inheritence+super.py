class Phone:
    # constructor
    def __init__(self,name,model,price):
        self.name = name
        self.model = model
        self.price = price


class ButtonPhone(Phone):
    # constructor
    def __init__(self,name,model,price,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        super().__init__(name,model,price)

class Android(Phone):
    # constructor
    def __init__(self,name,model,price,p,q,r):
        self.p = p
        self.q = q
        self.r = r
        super().__init__(name,model,price)

class Apple(Phone):
    # constructor
    def __init__(self,name,model,price,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        super().__init__(name,model,price)



print(Apple('Iphone','X',10000,1,2,3).z)
print(Apple('Iphone','X',10000,1,2,3).name)

