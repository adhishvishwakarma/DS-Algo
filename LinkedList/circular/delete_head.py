class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def delete_head(head):
    if not head:
        return
    if not head.next:
        return
    curr = head
    new_head = head.next
    while curr.next != head:
        curr = curr.next
    curr.next = new_head
    return new_head


def better_delete_head(head):
    if not head:
        return
    if not head.next:
        return
    head.data = head.next.data  # swapping data from next
    head.next = head.next.next  # Deleting next
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
# new_root = delete_head(root)
# print_list(new_root)
print_list(better_delete_head(root))

