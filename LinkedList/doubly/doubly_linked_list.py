class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedListAppend:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        node = Node(data)
        if self.head:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node
        self.size += 1


words = DoublyLinkedListAppend()
words.append('eggs')
words.append('ham')
words.append('spam')

current = words.head
while current:
    print(current.data)
    current = current.next


# Delete node
class DoublyLinkedListDelete:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        node = Node(data)
        if self.head:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node
        self.size += 1

    def delete(self, data):
        curr = self.head
        node_deleted = False
        if not curr:   # Item not found in the list
            node_deleted = False
        elif curr.data == data:  # Item at head
            self.head = curr.next
            self.head.prev = None
            node_deleted = True
        elif self.tail.data == data:  # Item at tail
            self.tail = self.tail.prev
            self.tail.next = None
            node_deleted = True
        else:   # Item in the middle
            while curr:
                if curr.data == data:
                    curr.prev.next = curr.next
                    curr.next.prev = curr.prev
                    node_deleted = True
                curr = curr.next
        if node_deleted:
            self.size -= 1


words = DoublyLinkedListDelete()
words.append('eggs')
words.append('ham')
words.append('only')
words.append('spam')
words.delete('ham')
words.delete('spam')
words.delete('eggs')

current = words.head
while current:
    print(current.data)
    current = current.next


# Iter and search
class DoublyLinkedListIterSearch:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        node = Node(data)
        if self.head:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        else:
            self.head = node
            self.tail = node
        self.size += 1

    def delete(self, data):
        curr = self.head
        deleted = False
        if not curr:
            deleted = False
        elif curr.data == data:
            self.head = curr.next
            self.head.prev = None
            deleted = True
        elif self.tail.data == data:
            self.tail = self.tail.prev
            self.tail.next = None
            deleted = True
        else:
            while curr:
                if curr.data == data:
                    curr.prev.next = curr.next
                    curr.next.prev = curr.prev
                    deleted = True
                curr = curr.next

        if deleted:
            self.size -= 1

    def iter(self):
        curr = self.head
        while curr:
            yield curr.data
            curr = curr.next

    def search(self, data):
        for node in self.iter():
            if node == data:
                return True
        return False


words = DoublyLinkedListIterSearch()
words.append('eggs')
words.append('ham')
words.append('only')
words.append('spam')
print(words.search('ham'))
print(words.search('pam'))

for i in words.iter():
    print(i)
