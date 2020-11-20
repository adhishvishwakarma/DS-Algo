class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Deque:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def insert_front(self, x):
        node = Node(x)
        if not self.front:
            self.front = node
        else:
            node.next = self.front
            self.front.prev = node
            self.front = node
        self.size += 1

    def insert_rear(self, x):
        node = Node(x)
        if not self.rear:
            self.front = node
        else:
            node.prev = self.rear
            self.rear.next = node
            self.rear = node
        self.size += 1

    def delete_front(self):
        if not self.front:
            return
        if not self.front.next:
            self.rear = None
            return
        tmp = self.front
        self.front = self.front.next
        self.front.prev = None
        self.size -= 1
        return tmp.data

    def delete_rear(self):
        if not self.rear:
            return
        if not self.rear.prev:
            return
        self.rear.prev.next = None
        self.rear = self.rear.prev
        self.size -= 1

    def get_front(self):
        return self.front

    def get_rear(self):
        return self.rear

    def is_empty(self):
        return True if not self.size else False

    def size(self):
        return self.size
