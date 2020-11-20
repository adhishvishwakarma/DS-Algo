class Queue:
    def __init__(self, c):
        self.l = [None] * c
        self.cap = c
        self.size = 0
        self.front = 0

    def get_front(self):
        if not self.size:
            return
        return self.l[self.front]

    def get_rear(self):
        if not self.size:
            return
        rear = (self.front + self.size - 1) % self.cap
        return self.l[rear]

    def enqueue(self, x):
        if self.size == self.cap:
            return
        rear = (self.front + self.size -1) % self.cap
        rear = (rear + 1) % self.cap
        self.l[rear] = x
        self.size += 1

    def dequeue(self):
        if not self.size:
            return
        res = self.l[self.front]
        self.front = (self.front + 1) % self.cap
        self.size -= 1
        return res
