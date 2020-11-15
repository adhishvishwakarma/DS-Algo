class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def insert(head, val):
    new_head = Node(val)
    new_head.next = head
    return new_head


root = Node(10)
root.next = Node(20)
root.next.next = Node(30)

x = insert(root, 5)
while x:
    print(x.data, end=' ')
    x = x.next
