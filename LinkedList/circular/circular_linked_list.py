class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class CircularLinkedListL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        node = Node(data)
        if self.head:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node
        self.tail.next = self.head
        self.size += 1


words = CircularLinkedListL()
words.append('eggs')
words.append('ham')
words.append('only')
words.append('spam')
current = words.head
while current:
    print(current.data)
    current = current.next
    

# Delete Node
class CircularLinkedListDelete:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        node = Node(data)
        if self.head:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node
        self.tail.next = self.head
        self.size += 1

    def delete(self, data):
        curr = self.tail
        prev = self.tail
        while prev == curr or prev != self.head:
            if curr.data == data:
                if curr == self.tail:
                    self.tail = curr.next
                    self.head.next = self.tail
                else:
                    prev.next = curr.next
                self.size -= 1
                return
            prev = curr
            curr = curr.next
