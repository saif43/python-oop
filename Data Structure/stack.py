class Stack:
    def __init__(self):
        self.stack = []

    def add(self,data):
        if data in self.stack:
            print(data,'is already in the stack')
            return
        self.stack.append(data)

    def peek(self):
        return self.stack[-1]

    def printAll(self):
        for i in self.stack:
            print(i)

    def remove(self):
        if len(self.stack) > 0:
            return self.stack.pop()
    
number = Stack()

number.add(1)
number.add(2)
number.add(3)

number.printAll()
print('--------')
print(number.remove())
print('--------')
number.printAll()
