class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


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


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = head
print_list(head)
