#!/usr/bin/env python


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


def is_valid_bst(root):
    """!
    Checks if the tree is a BST.
    Time complexity O(n)
    Space Complexity O(1)
    """
    if not root:
        return True
    stack = []
    prev = None
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        node = stack.pop()
        if prev and node.val <= prev.val:
            return False
        prev = node
        root = node.right
    return True


if __name__ == '__main__':
    root = Node(0)
    root.left = Node(1)
    root.right = Node(3)
    print('Given tree is BST: {0}'.format(is_valid_bst(root)))
    root = Node(1)
    root.left = Node(1)
    print('Given tree is BST: {0}'.format(is_valid_bst(root)))
    root = Node(5)
    root.left = Node(1)
    root.right = Node(4)
    root.right.left = Node(3)
    root.right.right = Node(6)
    print('Given tree is BST: {0}'.format(is_valid_bst(root)))