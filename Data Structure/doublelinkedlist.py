class Node:
    def __init__(self, datavalue=None):
        self.datavalue = datavalue
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def insertAtLast(self, data):
        data = Node(data)

        if self.head is None:
            self.head = data
            return
        
        temp = self.head

        while temp.next:
            temp = temp.next
        
        temp.next = data
        data.prev = temp

    def insertAtFirst(self, data):
        data = Node(data)

        if self.head is None:
            self.head = data
            return
        
        temp = self.head
        data.next = temp
        temp.prev = data
        self.head = data

    def printAll(self):
        temp = self.head
        while temp is not None:
            print(temp.datavalue)
            temp = temp.next

    def reverse(self):
        temp = self.head

        while temp.next:
            temp = temp.next

        while temp:
            print(temp.datavalue)
            temp = temp.prev

    def insertBetween(self,data1,data2,newvalue):
        newvalue = Node(newvalue)
        data1 = Node(data1)
        data2 = Node(data2)

        temp = self.head

        while temp.datavalue != data1.datavalue:
            temp = temp.next
        
        newvalue.next = data2
        newvalue.prev = temp

        temp.next = newvalue
        data2.prev = newvalue


week = DoubleLinkedList()

week.insertAtLast('Mon')
week.insertAtLast('Tue')
week.insertAtFirst('Sun')
week.insertAtLast('Thu')
week.insertBetween('Tue','Thu','Wed')


# week.printAll()
week.reverse()