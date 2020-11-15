class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


def insert(head, val):
    node = Node(val)
    if not head:
        return Node(val)
    node.next = head
    head.prev = node
    return node


root = Node(10)
root.next = Node(20)
root.next.next = Node(30)

root = insert(root, 40)

while root:
    print(root.data, end=' ')
    root = root.next
