#!/usr/bin/env python

class ListNode:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class ReverseLinkedList:
    def __init__(self) -> None:
        self.head = None    

    def insert(self, array):
        node = ListNode(array[0])
        temp = node
        for i in array[1:]:
            temp.next = ListNode(i)
            temp = temp.next

        return node

    def reverse(self, node):
        current = node
        prev = None
        while current:
            Next = current.next
            current.next = prev
            prev = current
            current = Next

        return prev

    def reverse_at_index(self, node, index):
        current = node
        Next = None
        prev = None
        count = 0
        while current and count < index:
            Next = current.next
            current.next = prev
            prev = current
            current = Next
            count += 1

        if Next:
            node.next = self.reverse_at_index(Next, index)

        return prev

    def print_list(self, node, name):
        temp = node
        print('{0}: '.format(name))
        while temp:
            print(temp.value, end=' ')
            temp = temp.next
        print('')


if __name__ == '__main__':
    llist = ReverseLinkedList()
    node = llist.insert([5, 6, 4, 2, 7, 1, 8])
    llist.print_list(node, 'node')
    reverse_node = llist.reverse(node)
    llist.print_list(reverse_node, 'reverse_node')
    node = llist.insert([5, 6, 4, 2, 7, 1, 8])
    reverse_index_node = llist.reverse_at_index(node, 3)
    llist.print_list(reverse_index_node, 'reverse_index_node')
