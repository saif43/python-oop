class Queue:
  def __init__(self, contents):
    self.__hiddenlist = list(contents)

  def push(self, value):
    self.__hiddenlist.insert(0, value)
   
  def pop(self):
    return self.__hiddenlist.pop(-1)

  def __repr__(self):
    return "Queue({})".format(self.__hiddenlist)

queue = Queue([1, 2, 3])
print(queue)
queue.push(0)

print(queue)
queue.pop()
print(queue)
print(queue.__hiddenlist)