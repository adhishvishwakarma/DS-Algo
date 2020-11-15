class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def search(head, val):
    c = 1
    while head:
        if head.data == val:
            return c
        head = head.next
        c += 1
    return -1


root = Node(10)
root.next = Node(20)
root.next.next = Node(30)

print(search(root, 30))