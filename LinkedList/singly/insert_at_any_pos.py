class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def insert(head, pos, val):
    node = Node(val)
    if pos == 1:
        node.next = head
        return node
    curr = head
    for i in range(pos - 2):
        curr = curr.next
        if not curr:
            return head
    node.next = curr.next
    curr.next = node
    return head


root = Node(10)
root.next = Node(20)
root.next.next = Node(30)

x = insert(root, 1, 40)

while x:
    print(x.data, end=' ')
    x = x.next
