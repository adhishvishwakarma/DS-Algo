class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


def add_node(head, p, data):
    # Code here
    node = Node(data)
    curr = head
    if not head:
        return node

    for i in range(p-1):
        curr = curr.next
    node.prev = curr
    node.next = curr.next
    if curr.next:
        curr.next.prev = node
    curr.next = node

    return head


root = Node(10)
root.next = Node(20)
root.next.next = Node(30)

root = add_node(root, 1, 40)

while root:
    print(root.data, end=' ')
    root = root.next
