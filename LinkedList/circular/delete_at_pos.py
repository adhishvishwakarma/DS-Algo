class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def delete(head, pos):
    if not head:
        return
    elif pos == 0 and head:
        head.data = head.next.data
        head.next = head.next.next
        return head
    elif not head.next and pos != 0:
        return head
    curr = head
    for i in range(pos-1):
        curr = curr.next
        if curr == head:
            return head
    curr.next = curr.next.next
    return head


def print_list(head):
    if not head:
        return
    if not head.next:
        print(head.data)
        return
    curr = head
    while curr:
        print(curr.data, end=' ')
        curr = curr.next
        if curr == head:
            break


root = Node(10)
root.next = Node(20)
root.next.next = Node(30)
root.next.next.next = root
print_list(delete(root, 0))
