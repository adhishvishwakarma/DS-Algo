# three forms of depth first traversal, namely in-order, pre-order and post-order


class Node:
    def __init__(self, data):
        self.data = data
        self.right_child = None
        self.left_child = None


a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")
f = Node("F")
g = Node("G")
h = Node("H")

a.left_child = b
a.right_child = c
b.left_child = d
b.right_child = e
d.left_child = g
d.right_child = h
c.right_child = f

# current = a
# while current:
#     print(current.data)
#     current = current.left_child
#
# print("\n")


class Tree:
    def inorder(self, root_node):
        curr = root_node
        if not curr:
            return
        self.inorder(curr.left_child)
        print(curr.data)
        self.inorder(curr.right_child)

    def preorder(self, root_node):
        curr = root_node
        if not curr:
            return
        print(curr.data)
        self.preorder(curr.left_child)
        self.preorder(curr.right_child)

    def postorder(self, root_node):
        curr = root_node
        if not curr:
            return
        self.postorder(curr.left_child)
        self.postorder(curr.right_child)
        print(curr.data)


t = Tree()
t.inorder(a)
t.preorder(a)
t.postorder(a)
