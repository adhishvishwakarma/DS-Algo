class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def get_length(head):
    c = 0
    if not head:
        return
    if not head.next:
        return 1
    curr = head
    while curr:
        curr = curr.next
        c += 1
        if curr == head:
            break
    return c


root = Node(10)
root.next = Node(20)
root.next.next = Node(30)
root.next.next.next = root
print(get_length(root))
