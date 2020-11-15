class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def insert_end(head, val):
    if not head:
        return Node(val)
    curr = head
    while curr.next:
        curr = curr.next
    curr.next = Node(val)
    return head


root = Node(10)
root.next = Node(20)
root.next.next = Node(30)

insert_end(root, 40)

while root:
    print(root.data, end=' ')
    root = root.next
