class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def find_middle(head):
    c = 1
    curr = head
    while curr:
        curr = curr.next
        c += 1
        if curr == head:
            break
    mid = c//2
    cur = head
    for i in range(mid-1):
        cur = cur.next
    return cur.data


root = Node(10)
root.next = Node(20)
root.next.next = Node(30)
root.next.next.next = root
print(find_middle(root))
