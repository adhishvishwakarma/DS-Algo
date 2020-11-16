class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def circular(head):
    if not head:
        return False
    curr = head
    while curr:
        curr = curr.next
        if curr == head:
            return True
    return False


root = Node(10)
root.next = Node(20)
root.next.next = Node(30)
root.next.next.next = root
print(circular(root))
