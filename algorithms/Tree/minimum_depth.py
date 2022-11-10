#!/usr/bin/env python


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


def min_depth(root):
    """!
    Calculates the minimum depth of a binary tree.
    Time complexity O(2**d)
    Space Complexity O(1)
    """
    if not root:
        return 0
    
    depth = 1
    q = [[root, depth]]
    while q:
        root, depth = q.pop(0)
        if not root.left and not root.right:
            return depth
        if root.left:
            q.append([root.left, depth+1])
        if root.right:
            q.append([root.right, depth+1])


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print(min_depth(root))