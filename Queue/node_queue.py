# Doubly linked list implementation

class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, data):
        node = Node(data)
        if self.head:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node
        self.size += 1

    def dequeue(self):
        if self.size == 1:
            self.head = None
            self.tail = None
            self.size = 0
        elif self.size > 1:
            self.head = self.head.next
            self.head.prev = None
            self.size -= 1
