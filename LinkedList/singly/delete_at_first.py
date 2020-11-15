class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def delete_first(head):
    if not head:
        return
    new_head = head.next
    head.next = None
    return new_head


root = Node(10)
root.next = Node(20)
root.next.next = Node(30)

root = delete_first(root)

while root:
    print(root.data, end=' ')
    root = root.next
