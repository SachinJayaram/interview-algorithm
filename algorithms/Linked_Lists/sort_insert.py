#!/usr/bin/env python

class ListNode:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def sorted_insert(self, node):
        if not self.head or self.head.value >= node.value:
            node.next = self.head
            self.head = node
        else:
            temp = self.head
            while temp.next and temp.next.value < node.value:
                temp = temp.next
            node.next = temp.next
            temp.next = node

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value, end=' ')
            temp = temp.next


if __name__ == '__main__':
    llist = LinkedList()
    new_node = ListNode(5)
    llist.sorted_insert(new_node)
    new_node = ListNode(8)
    llist.sorted_insert(new_node)
    new_node = ListNode(3)
    llist.sorted_insert(new_node)
    new_node = ListNode(6)
    llist.sorted_insert(new_node)
    new_node = ListNode(4)
    llist.sorted_insert(new_node)
    llist.print_list()