class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def sorted_or_not(head):
    if not head:
        return
    if not head.next:
        return True
    curr = head
    if curr.data < curr.next.data:
        while curr.next:
            if not curr.data <= curr.next.data:
                return False
            curr = curr.next
    elif curr.data > curr.next.data:
        while curr.next:
            if not curr.data >= curr.next.data:
                return False
            curr = curr.next
    return True


root = Node(10)
root.next = Node(20)
root.next.next = Node(30)

print(sorted_or_not(root))

