class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def insert(head, pos, data):
    node = Node(data)
    if not head and pos == 0:
        node.next = node
        return node
    elif not head and pos != 0:
        return
    if pos == 0:
        node.next = head.next
        head.next = node
        head.data, node.data = node.data, head.data
        return head
    curr = head
    for i in range(pos-1):
        curr = curr.next
        if curr == head:
            return head
    node.next = curr.next
    curr.next = node
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
new_root = insert(None, 1, 40)
# newest_root = insert_constant_time(new_root, 50)
print_list(new_root)
