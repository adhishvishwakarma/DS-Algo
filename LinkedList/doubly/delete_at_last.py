class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


def delete_tail(head):
    if not head:
        return
    if not head.next:
        return

    curr = head
    while curr.next.next:
        curr = curr.next
    curr.next.prev = None
    curr.next = None
    return head


root = Node(10)
root.next = Node(20)
root.next.next = Node(30)

root = delete_tail(root)

while root:
    print(root.data, end=' ')
    root = root.next

