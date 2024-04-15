class Node:
    def __init__(self, data, next_item=None) -> None:
        self.data = data
        self.next = next_item

    def __str__(self) -> str:
        '''string'''
        stringa = ""
        if not self:
            stringa += "None"
        else:
            probe = self
            while probe:
                if probe.next:
                    stringa = stringa + str(probe.data) + " -> "
                else:
                    stringa += str(probe.data)
                probe = probe.next
            stringa += " -> None"
        return stringa
class Queue:

    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def add(self, item):
        if self.head is None:
            self.tail = Node(item)
            self.head = self.tail
        else:
            self.tail.next = Node(item)
            self.tail = self.tail.next

    def pop(self):
        if self.head:
            item = self.head.data
            self.head = self.head.next
            return item
        raise ValueError('Queue is empty.')

    @property
    def peek(self):
        return self.tail.data

    def __len__(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def __str__(self):
        s = ''
        current = self.head
        while current is not None:
            s += str(current.data)+' '
            current = current.next
        return f'start -> {s}<- end'


class MyStack:
    def __init__(self):
        self.enqueue = Queue()
        self.dequeue = Queue()

    def push(self, x: int) -> None:
        self.enqueue.add(x)

    def pop(self) -> int:
        if self.enqueue.head is not None:
            length_1 = len(self.enqueue)
            for _ in range(length_1 - 1):
                self.dequeue.add(self.enqueue.pop())
            popped = self.enqueue.pop()
            self.enqueue, self.dequeue = self.dequeue, self.enqueue
            return popped

    def top(self) -> int:

        return self.enqueue.peek

    def empty(self) -> bool:
        return self.dequeue.is_empty() and self.enqueue.is_empty()
