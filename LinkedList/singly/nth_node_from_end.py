class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def nth_node_from_last(head, n):
    l = []
    curr = head
    while curr:
        l.append(curr.data)
        curr = curr.next
    if n > len(l):
        return -1
    else:
        return l[len(l) - n]


root = Node(10)
root.next = Node(20)
root.next.next = Node(30)

print(nth_node_from_last(root, 2))
