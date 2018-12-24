from collections import deque


class BiTreeNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None


a = BiTreeNode('A')
b = BiTreeNode('B')
c = BiTreeNode('C')
d = BiTreeNode('D')
e = BiTreeNode('E')
f = BiTreeNode('F')
g = BiTreeNode('G')

e.lchild = a
e.rchild = g
a.rchild = c
c.lchild = b
c.rchild = d
g.rchild = f

root = e


def pre_order(root):
    if root:
        print(root.data, end='')
        pre_order(root.lchild)
        pre_order(root.rchild)


def in_order(root):
    if root:
        in_order(root.lchild)
        print(root.data, end='')
        in_order(root.rchild)


def post_order(root):
    if root:
        post_order(root.lchild)
        post_order(root.rchild)
        print(root.data, end='')


def level_order(root):
    q = deque()
    q.append(root)
    while len(q) > 0:
        node = q.popleft()
        print(node.data, end='')
        if node.lchild:
            q.append(node.lchild)
        if node.rchild:
            q.append(node.rchild)


print(pre_order(root))
level_order(root)
