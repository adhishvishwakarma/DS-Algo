class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def delete(head, pos):
    if not head:
        return
    if pos == 0:
        return head.next
    curr = head
    for i in range(pos-1):
        curr = curr.next
    curr.next = curr.next.next
    return head


root = Node(10)
root.next = Node(20)
root.next.next = Node(30)

root = delete(root, 1)

while root:
    print(root.data, end=' ')
    root = root.next
