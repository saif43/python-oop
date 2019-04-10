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

    def insertAtFirst(self, data):
        if self.headValue is None:
            self.headValue = Node(data)
            return
        
        temp = self.headValue
        data = Node(data)
        data.nextvalue = temp
        self.headValue = data
        

    def insertBetween(self, data1, data2, newdata):
        newdata = Node(newdata)
        data1 = Node(data1)
        data2 = Node(data2)

        temp = self.headValue

        while temp.datavalue != data1.datavalue:
            temp =  temp.nextvalue
        
        newdata.nextvalue = data2
        temp.nextvalue = newdata


    def delete(self, data):
        data = Node(data)

        temp = self.headValue

        while temp.nextvalue.datavalue != data.datavalue:
            temp =  temp.nextvalue
        
        temp.nextvalue = temp.nextvalue.nextvalue


    def search(self, data):
        temp = self.headValue

        while temp is not None:
            if temp.datavalue == data:
                print(data,'Found')
                return
            temp =  temp.nextvalue
            
            if temp is None:
                print(data,'not found')
        

    def reverse(self):
        if self.headValue is None:
            return

        temp = self.headValue
 
        data = temp.datavalue

        self.headValue = temp.nextvalue

        self.reverse()

        print(data)





        

    def printAll(self):
        temp = self.headValue
        while(temp is not None):
            print(temp.datavalue)
            temp = temp.nextvalue

week = SingleLinkedList()

week.insertAtLast('Tue')
week.insertAtFirst('Sun')
week.insertBetween('Sun','Tue','Mon')
week.insertAtLast('Fri')

week.delete('Fri')
week.printAll()

# week.reverse()