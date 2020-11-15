class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def insert_linear(head, val):
    node = Node(val)
    if not head:
        return node
    elif val < head.data:
        node.next = head
        return node
    curr = head
    while curr.next:
        if curr.data < val <= curr.next.data:
            node.next = curr.next
            curr.next = node
            return head
        curr = curr.next
    curr.next = node
    return head


root = Node(10)
root.next = Node(20)
root.next.next = Node(30)

root = insert_linear(root, 25)

while root:
    print(root.data, end=' ')
    root = root.next
