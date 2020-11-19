from collections import deque


class DequeQueue:
    def __init__(self):
        self.items = deque()
        self.size = 0

    def enqueue(self, data):
        self.items.append(data)
        self.size += 1

    def dequeue(self):
        data = self.items.popleft()
        self.size -= 1
        return data


q = DequeQueue()
print(q.items)
print(q.size)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q.items)
print(q.size)
print(q.dequeue())
print(q.items)
print(q.size)
