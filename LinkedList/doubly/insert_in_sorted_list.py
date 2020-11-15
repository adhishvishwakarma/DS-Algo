class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


def insert_at_pos(head, x):
    node = Node(x)
    if not head:
        return
    if x < head.data:
        node.next = head
        head.prev = node
        return node
    curr = head
    while curr.next:
        if curr.data < x <= curr.next.data:
            node.next = curr.next
            node.prev = curr
            curr.next.prev = node
            curr.next = node
            return head
        curr = curr.next
    curr.next = node
    node.prev = curr
    return head


root = Node(10)
root.next = Node(20)
root.next.next = Node(30)

root = insert_at_pos(root, 40)

while root:
    print(root.data, end=' ')
    root = root.next

