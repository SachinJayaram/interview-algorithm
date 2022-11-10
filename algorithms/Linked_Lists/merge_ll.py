#!/usr/bin/env python

class ListNode:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class MergeLinkedList:
    def __init__(self) -> None:
        self.head1 = None
        self.head2 = None

    def merge(self, node1, node2):
        p_curr = node1
        q_curr = node2
        while p_curr and q_curr:
            p_next = p_curr.next
            q_next = q_curr.next
            q_curr.next = p_next
            p_curr.next = q_curr
            p_curr = p_next
            q_curr = q_next
        node2 = q_curr

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
        current = prev

        return current

    def print_list(self, node):
        temp = node
        while temp:
            print(temp.value, end=' ')
            temp = temp.next
        print('')


if __name__ == '__main__':
    array1 = [5, 7, 17, 13, 11]
    array2 = [12, 10, 2, 4, 6]
    llist = MergeLinkedList()
    Node1 = llist.insert(array1)
    Node2 = llist.insert(array2)
    print('Node1: ')
    llist.print_list(Node1)
    print('Node2: ')
    llist.print_list(Node2)
    llist.merge(Node1, Node2)
    llist.print_list(Node1)
    Node3 = llist.reverse(Node1)
    llist.print_list(Node3)