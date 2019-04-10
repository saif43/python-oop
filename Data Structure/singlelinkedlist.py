class Node:
    def __init__(self, datavalue=None):
        self.datavalue = datavalue
        self.nextvalue = None

class SingleLinkedList:
    def __init__(self):
        self.headValue = None
    
    def insertAtLast(self, data):
        if self.headValue is None:
            self.headValue = Node(data)
            return
        
        temp = self.headValue

        while(temp.nextvalue):
            temp = temp.nextvalue
        
        temp.nextvalue = Node(data)
        