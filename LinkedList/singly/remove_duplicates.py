class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def remove_dupes(head):
    if not head:
        return
    curr = head
    while curr.next:
        if curr.data == curr.next.data:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head


root = Node(10)
root.next = Node(10)
root.next.next = Node(30)

root = remove_dupes(root)

while root:
    print(root.data, end=' ')
    root = root.next
