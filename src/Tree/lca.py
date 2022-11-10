#!/usr/bin/env python

class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

def lowestCommonAncestor(root: 'Node', p: 'Node', q: 'Node') -> 'Node':
    if root.val < p.val and root.val < q.val:
        return lowestCommonAncestor(root.right, p, q)
    elif root.val > p.val and root.val > q.val:
        return lowestCommonAncestor(root.left, p, q)
    else:
        return root

if __name__ == '__main__':    
    root = Node(6)
    root.left = Node(2)
    root.right = Node(8)
    root.left.left = Node(0)
    root.left.right = Node(4)
    root.left.right.left = Node(3)
    root.left.right.right = Node(5)
    root.right.left = Node(7)
    root.right.right = Node(9)
    p = Node(2)
    q = Node(8)
    print(lowestCommonAncestor(root, p, q).val)
    p = Node(2)
    q = Node(4)
    print(lowestCommonAncestor(root, p, q).val)