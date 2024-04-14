class Node:
    def __init__(self, data, next_item=None):
        self.data = data
        self.next = next_item

class Stack:
    def __init__(self) -> None:
        self.head = None

    def __len__(self):
        probe = self.head
        counter = 0
        while probe:
            counter += 1
            probe = probe.next
        return counter

    def is_empty(self):
        return not self.head

    def push(self, data):
        self.head = Node(data, self.head)

    @property
    def peek(self):
        if self.head:
            return self.head.data
        return None

    def pop(self):
        popped = self.head.data
        self.head = self.head.next
        return popped

    def __str__(self) -> str:
        stringa = ''
        probe = self.head
        while probe:
            stringa = str(probe.data) + ' ' + stringa
            probe = probe.next
        return 'bottom -> ' + stringa + '<- top'

class MyQueue:

    def __init__(self):
        self.enqueue = Stack()
        self.dequeue = Stack()

    def push(self, x: int) -> None:
        self.enqueue.push(x)

    def pop(self) -> int:
        while not self.enqueue.is_empty():
            self.dequeue.push(self.enqueue.pop())

        return self.dequeue.pop()

    def peek(self) -> int:
        while not self.enqueue.is_empty():
            self.dequeue.push(self.enqueue.pop())
        return self.dequeue.peek

    def empty(self) -> bool:
        return self.enqueue.is_empty() and self.dequeue.is_empty()

myQueue = MyQueue()
myQueue.push(1) #queue is: [1]
print(myQueue.enqueue)
myQueue.push(2) #queue is: [1, 2] (leftmost is front of the queue)
print(myQueue.enqueue)
assert myQueue.peek() == 1, myQueue.peek() #return 1
print(myQueue.enqueue)
assert myQueue.pop() == 1, myQueue.pop() #return 1, queue is [2]
myQueue.empty() #return false
