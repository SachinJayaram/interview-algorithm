#!/usr/bin/env python


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


def in_order(root):    
    """!
    prints the data inorder.
    Time complexity O(n)
    Space Complexity O(1)
    """
    if not root:
        return None
    in_order(root.left)
    print(root.data, end=' ')
    in_order(root.right)


def pre_order(root):    
    """!
    prints the data inorder.
    Time complexity O(n)
    Space Complexity O(1)
    """
    if not root:
        return None
    print(root.data, end=' ')
    pre_order(root.left)
    pre_order(root.right)


def post_order(root):    
    """!
    prints the data inorder.
    Time complexity O(n)
    Space Complexity O(1)
    """
    if not root:
        return None
    post_order(root.left)
    post_order(root.right)
    print(root.data, end=' ')


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print('InOrder traversal')
    in_order(root)
    print('')
    print('Preorder traversal')
    pre_order(root)
    print('')
    print('Postorder traversal')
    post_order(root)