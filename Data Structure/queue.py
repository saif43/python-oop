class Queue:
    def __init__(self):
        self.queue = []

    def push(self, data):
        if data not in self.queue:
            self.queue.insert(0,data)
            return
        print(data,'already is in queue')
    
    def printAll(self):
        for i in self.queue:
            print(i)

    def remove(self):
        return self.queue.pop()


numbers = Queue()

numbers.push(1)
numbers.push(2)
numbers.push(3)


print(numbers.remove(),'removed')
numbers.printAll()