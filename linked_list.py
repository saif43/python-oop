class Node:
    def __init__(self, dataval=None):
        self.datavalue = dataval
        self.nextvalue = None

class SingleLinkedList:
    def __init__(self):
        self.headvalue = None

    def listPrint(self):
        node = self.headvalue

        while node is not None:
            print(node.datavalue)
            node = node.nextvalue
    
    def insertAtbeginning(self,newdata):
        newNode = Node(newdata)

        newNode.nextvalue = self.headvalue
        self.headvalue = newNode
    
    def insertAtLast(self, newdata):
        newNode = Node(newdata)

        if self.nextvalue is None:
            self.headvalue = newdata
            return
        
        temp = self.headvalue

        while temp.nextvalue is not None:
            temp = temp.nextvalue
        
        temp.nextvalue = newNode




family = SingleLinkedList()

family.headvalue = Node('Dad')

node1 = Node('Son')

family.headvalue.nextvalue = node1

node2 = Node('GrandSon')

node1.nextvalue = node2

family.listPrint()

print('==========')

family.insertAtbeginning('Dads dad')

family.insertAtLast('Grand grand son')

family.listPrint()