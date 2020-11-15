class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


def delete_head(head):
    if not head:
        return
    if not head.next:
        return

    new_head = head.next
    new_head.prev = None
    head.next = None
    return new_head


root = Node(10)
root.next = Node(20)
root.next.next = Node(30)

root = delete_head(root)

while root:
    print(root.data, end=' ')
    root = root.next

