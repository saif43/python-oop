def attach_description(func):
    func.description = 'This is function for addition'
    return func

@attach_description

def add(x,y):
    return x+y



print(add(2,3))
print(add.description)
