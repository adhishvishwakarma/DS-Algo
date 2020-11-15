class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


def insert_at_last(head, val):
    node = Node(val)
    if not head:
        return Node(val)
    curr = head
    while curr.next:
        curr = curr.next
    curr.next = node
    node.prev = curr
    return head


root = Node(10)
root.next = Node(20)
root.next.next = Node(30)

root = insert_at_last(root, 40)

while root:
    print(root.data, end=' ')
    root = root.next

