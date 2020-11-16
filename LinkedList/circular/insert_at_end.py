class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def delete(head):
    if not head:
        return
    if not head.next:
        return
    curr = head
    while curr.next.next != head:
        curr = curr.next
    curr.next.next = None
    curr.next = head
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
new_root = delete(root)
print_list(new_root)
