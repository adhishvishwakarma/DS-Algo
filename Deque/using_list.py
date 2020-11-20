class Deque:
    def __init__(self, c):
        self.front = None
        self.size = 0
        self.l = [None] * c
        self.cap = c

    def insert_front(self, x):
        if self.size == self.cap:
            return
        self.front = (self.front - 1) % self.cap
        self.l[self.front] = x
        self.size += 1

    def insert_rear(self, x):
        if self.size == self.cap:
            return
        new_rear = (self.front + self.size) % self.cap
        self.l[new_rear] = x
        self.size += 1

    def delete_front(self):
        if not self.size:
            return
        res = self.l[self.front]
        self.front = (self.front + 1) % self.cap
        self.size -= 1
        return res

    def delete_rear(self):
        if not self.size:
            return
        rear = (self.front + self.size - 1) % self.cap
        self.size -= 1
        return self.l[rear]

    def size(self):
        return self.size

    def is_empty(self):
        return True if not self.size else False
