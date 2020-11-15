class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


def reversing(head):
    if not head:
        return
    if not head.next:
        return head

    curr = head
    prev = None
    while curr:
        prev = curr
        curr.next, curr.prev = curr.prev, curr.next
        curr = curr.prev
    return prev


root = Node(10)
root.next = Node(20)
root.next.next = Node(30)

root = reversing(root)

while root:
    print(root.data, end=' ')
    root = root.next
