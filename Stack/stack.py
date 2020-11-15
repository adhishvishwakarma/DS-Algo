class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        node = Node(data)
        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node
        self.size += 1

    def pop(self):
        if self.top:
            data = self.top.data
            self.size -= 1
            if self.top.next:
                self.top = self.top.next
            else:
                self.top = None
            return data
        else:
            return None

    def peek(self):
        if self.top:
            return self.top.data
        else:
            return None

    # def contains(self, top, data):
    #     self.top = top
    #     if self.top:
    #         return True
    #     if self.top.next:
    #         return self.contains(self.top.next, data)
    #
    #     return None


stack = Stack()
stack.push(8)
stack.push(9)
stack.push(10)
print(stack.contains(8, 8))
print(stack.contains(8, 9))
print(stack.contains(8, 10))
print(stack.contains(8, 11))
