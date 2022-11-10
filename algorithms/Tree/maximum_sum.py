#!/usr/bin/env python


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


def max_sum(root):    
    """
    Calculates the sum of a single path in a given binary tree.
    Time complexity O(n)
    Space Complexity O(1)
    """
    if not root:
        return 0


if __name__ == '__main__':
    root = Node(10)
    root.left = Node(2)
    root.right = Node(10)
    root.left.left = Node(1)
    root.right.right = Node(-25)
    root.right.right.left   = Node(3)
    root.right.right.right  = Node(4)
    print(max_sum(root))
    print(max_sum.__doc__)