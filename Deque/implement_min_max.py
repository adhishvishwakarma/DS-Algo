from collections import deque


class DS:
    def __init__(self):
        self.dq = deque()

    def insert_min(self, x):
        self.dq.appendleft(x)

    def insert_max(self, x):
        self.dq.append(x)

    def extract_min(self):
        return self.dq.popleft()

    def extract_max(self):
        return self.dq.pop()

    def get_max(self):
        return self.dq[-1]

    def get_min(self):
        return self.dq[0]
