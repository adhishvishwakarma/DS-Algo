class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


def is_circular(head):
    if not head:
        return False
    curr = head
    while curr:
        curr = curr.next
        if curr == head:
            return True
    return False
