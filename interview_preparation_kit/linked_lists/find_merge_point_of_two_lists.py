#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the findMergeNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def compare_nodes(head, llist):
    temp_llist = llist 
    while llist:
        if llist and llist == head:
            return llist.data
        elif llist:
            llist = llist.next
    llist = temp_llist
    return None

def findMergeNode(head1, head2):
    while head1:
        if head1:
            result = compare_nodes(head1, head2)
            if result:
                return result
            head1 = head1.next
    return

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = 1

    for tests_itr in range(tests):
        index = 2

        llist1_count = 3

        llist1 = SinglyLinkedList()

        a = [1, 2, 3]
        for i in a:
            llist1_item = i
            llist1.insert_node(llist1_item)
            
        llist2_count = 2

        llist2 = SinglyLinkedList()

        b = [1, 3]
        for j in b:
            llist2_item = j
            llist2.insert_node(llist2_item)
            
        ptr1 = llist1.head
        ptr2 = llist2.head

        for i in range(llist1_count):
            if i < index:
                ptr1 = ptr1.next
                
        for i in range(llist2_count):
            if i != llist2_count-1:
                ptr2 = ptr2.next

        ptr2.next = ptr1

        result = findMergeNode(llist1.head, llist2.head)
        print(result, 'end')

    #     fptr.write(str(result) + '\n')

    # fptr.close()