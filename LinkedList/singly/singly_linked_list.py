class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


n1 = Node('eggs')
n2 = Node('ham')
n3 = Node('spam')

n1.next = n2
n2.next = n3

# Traversing the list
current = n1
while current:
    print(current.data)
    current = current.next


# Creating a class and adding methods
class SinglyLinkedListAppend:

    def __init__(self):
        self.tail = None

    def append(self, data):
        node = Node(data)
        if not self.tail:
            self.tail = node
        else:
            curr = self.tail
            while curr.next:
                curr = curr.next
            curr.next = node


words = SinglyLinkedListAppend()
words.append('egg')
words.append('ham')
words.append('spam')

current = words.tail
while current:
    print(current.data)
    current = current.next


# Faster append
class SinglyLinkedListFasterAppend:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        node = Node(data)
        if self.head:
            self.head.next = node
            self.head = node
        else:
            self.tail = node
            self.head = node


words = SinglyLinkedListFasterAppend()
words.append('egg')
words.append('ham')
words.append('spam')

current = words.tail
while current:
    print(current.data)
    current = current.next


# With Size
class SinglyLinkedListSize:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        node = Node(data)

        if self.head:
            self.head.next = node
            self.head = node
        else:
            self.head = node
            self.tail = node
        self.size += 1


words = SinglyLinkedListSize()
words.append('egg')
words.append('ham')
words.append('spam')

print(words.size)


# Better list traversal
class SinglyLinkedListTraversal:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        node = Node(data)
        if self.head:
            self.head.next = node
            self.head = node
        else:
            self.tail = node
            self.head = node
        self.size += 1

    def iter(self):
        curr = self.tail
        while curr:
            yield curr.data
            curr = curr.next


words = SinglyLinkedListTraversal()
words.append('egg')
words.append('ham')
words.append('spam')

for i in words.iter():
    print(i)


# Delete Node
class SinglyLinkedListDeleteNode:
    def __init__(self):
        self.tail = None
        self.head = None
        self.size = 0

    def append(self, data):
        node = Node(data)
        if self.head:
            self.head.next = node
            self.head = node
        else:
            self.head = node
            self.tail = node
        self.size += 1

    def iter(self):
        curr = self.tail
        while curr:
            yield curr.data
            curr = curr.next

    def delete(self, data):
        curr = self.tail
        prev = self.tail
        while curr:
            if curr.data == data:
                if curr == self.tail:
                    self.tail = curr.next
                else:
                    prev.next = curr.next
                self.size -= 1
                return
            prev = curr
            curr = curr.next


words = SinglyLinkedListDeleteNode()
words.append('egg')
words.append('ham')
words.append('spam')
words.delete('ham')

for i in words.iter():
    print(i)


# Search
class SinglyLinkedListSearch:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        node = Node(data)
        if self.head:
            self.head.next = node
            self.head = node
        else:
            self.head = node
            self.tail = node
        self.size += 1

    def iter(self):
        curr = self.tail
        while curr:
            yield curr.data
            curr = curr.next

    def delete(self, data):
        curr = self.tail
        prev = self.tail
        while curr:
            if curr.data == data:
                if curr == self.tail:
                    self.tail = curr.next
                else:
                    prev.next = curr.next
                self.size -= 1
                return
            prev = curr
            curr = curr.next

    def search(self, data):
        for node in self.iter():
            if data == node:
                return True
        return False


words = SinglyLinkedListSearch()
words.append('eggs')
words.append('ham')
words.append('spam')
print(words.search('eggs'))
print(words.search('pam'))


# clear list
class SinglyLinkedListClear:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        node = Node(data)
        if self.head:
            self.head.next = node
            self.head = node
        else:
            self.head = node
            self.tail = node
        self.size += 1

    def iter(self):
        curr = self.tail
        while curr:
            yield curr.data
            curr = curr.next

    def delete(self, data):
        curr = self.tail
        prev = self.tail
        while curr:
            if curr.data == data:
                if curr == self.tail:
                    self.tail = curr.next
                else:
                    prev.next = curr.next
            prev = curr
            curr = curr.next

    def search(self, data):
        for node in self.iter():
            if node == data:
                return True
        return False

    def clear(self):
        self.head = None
        self.tail = None


words = SinglyLinkedListClear()
words.append('eggs')
words.append('ham')
words.append('spam')
words.delete('eggs')
print(words.search('eggs'))
print(words.search('pam'))
words.clear()
for i in words.iter():
    print(i)
