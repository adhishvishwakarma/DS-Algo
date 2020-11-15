class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


def delete_node(head, x):
    # Code here
    if x == 1:
        new_head = head.next
        new_head.prev = None
        return new_head

    curr = head
    for i in range(x - 2):
        curr = curr.next

    if not curr.next.next:
        curr.next = None
    else:
        curr.next.next.prev = curr
        curr.next = curr.next.next

    return head


root = Node(10)
root.next = Node(20)
root.next.next = Node(30)

root = delete_node(root, 3)

while root:
    print(root.data, end=' ')
    root = root.next

