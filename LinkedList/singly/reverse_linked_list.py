class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reversing_pointers(head):
    if not head:
        return
    elif not head.next:
        return head

    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev, curr = curr, nxt
    return prev


def reverse_recursion(head):
    if not head:
        return
    if not head.next:
        return head
    rest_head = reverse_recursion(head.next)
    rest_tail = head.next
    rest_tail.next = head
    head.next = None
    return rest_head


def reverse_recursion_2(head, prev=None):
    if not head:
        return prev
    curr = head
    nxt = curr.next
    curr.next = prev
    return reverse_recursion_2(nxt, curr)


root = Node(10)
root.next = Node(20)
root.next.next = Node(30)

# root = reversing_pointers(root)
root = reverse_recursion_2(root)

while root:
    print(root.data, end=' ')
    root = root.next
