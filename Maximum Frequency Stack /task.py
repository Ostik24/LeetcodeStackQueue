class Node:
    def __init__(self, data, next_item=None):
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
        if self.head:
            self.head = Node(data, self.head)
        else:
            self.head = Node(data)

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

class FreqStack:
    def __init__(self):
        self.stack = Stack()
        self.freq = {}
        self.freq_nodes = {}
        self.max_freq = 0

    def push(self, val: int) -> None:
        self.freq[val] = self.freq.get(val, 0) + 1
        freq = self.freq[val]
        self.max_freq = max(self.max_freq, freq)

        if freq not in self.freq_nodes:
            self.freq_nodes[freq] = Node(val)
        else:
            node = Node(val)
            node.next = self.freq_nodes[freq]
            self.freq_nodes[freq] = node

        self.stack.push(val)

    def pop(self) -> int:
        val = self.freq_nodes[self.max_freq].data
        self.freq_nodes[self.max_freq] = self.freq_nodes[self.max_freq].next
        self.freq[val] -= 1
        if self.freq_nodes[self.max_freq] is None:
            self.max_freq -= 1

        return val
