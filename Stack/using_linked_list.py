class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class MyStack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            self.size += 1
            return self.head
        node.next = self.head
        self.head = node
        self.size += 1
        return self.head

    def pop(self):
        if not self.head:
            return
        if not self.head.next:
            return
        res = self.head.data
        self.head = self.head.next
        self.size -= 1
        return res

    def peek(self):
        return self.head.data if self.head else None

    def length(self):
        return self.size

    def print_stack(self):
        curr = self.head
        while curr:
            print(curr.data, end=' ')
            curr = curr.next


s = MyStack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.print_stack()
print(s.length())
s.pop()
s.print_stack()
print(s.length())
print(s.peek())
print(s.length())
