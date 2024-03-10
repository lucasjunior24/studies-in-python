class Queue:
  def __init__(self) -> None:
    self.items = []
    self.position = 0

  def __str__(self) -> str:
    return str(self.items)

  def dequeue(self):
    if self.is_empty():
      return "A Queue está vazia"
    item = self.items[0]
    self.position -= 1

    del self.items[0]
    return item


  def is_empty(self):
    return self.items == []

  def enqueue(self, value):
      self.items = self.items + [value]
      self.position += 1


queue = Queue()
print(queue)
print(queue.is_empty())
queue.enqueue("8")
queue.enqueue("12")
queue.enqueue("20")
queue.enqueue("25")
print(queue)
print(queue.is_empty())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue)
print(queue.position)
queue.enqueue("20")
queue.enqueue("25")
print(queue)
print(queue.position)