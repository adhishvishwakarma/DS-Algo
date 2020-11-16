class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def insert(head, data):
    node = Node(data)
    if not head:
        node.next = node
        return node
    curr = head
    while curr.next != head:
        curr = curr.next
    curr.next = node
    node.next = head
    return node


def insert_constant_time(head, val):
    node = Node(val)
    if not head:
        node.next = node
        return node
    node.next = head.next
    head.next = node
    head.data, node.data = node.data, head.data
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
new_root = insert(root, 40)
newest_root = insert_constant_time(new_root, 50)
print_list(newest_root)
