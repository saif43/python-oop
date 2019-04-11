class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self,data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            else:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
            
    
    
    
    
    def printAll(self):
        if self.left:
            self.left.printAll()
        print(self.data)
        if self.right:
            self.right.printAll()

    def find(self, data):
        if data < self.data:
            if self.left is None:
                return str(data)+' not found'
            return self.left.find(data)

        elif data > self.data:
            if self.right is None:
                return str(data)+' not found'
            return self.right.find(data)
        
        else:
            return str(data)+' is found'
    
            


root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)

root.printAll()

print(root.find(34))
print(root.find(14))



