# Reference: https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/
from typing import Optional

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def inorder(root: Optional[Node], func):
    if root is not None:
        inorder(root.left, func)
        func(root)
        inorder(root.right, func)

def insert(node, key):
    if node is None:
        # Empty tree
        return Node(key)

    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)

    return node


def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left

    return current

def deleteNode(root, key):
    if root is None:
        return root

    if key < root.key:
        root.left = deleteNode(root.left, key)
    elif key > root.key:
        root.right = deleteNode(root.right, key)
    else:
        # Same key, node to be deleted

        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = minValueNode(root.right)
        root.key = temp.key
        root.right = deleteNode(root.right, temp.key)

    return root

root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)

inorder(root, lambda node: print(node.key,node.left.key if node.left else None, node.right.key if node.right else None))
