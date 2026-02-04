import unittest
from codinginterviewprep.fastandslowpointers.linked_list_midpoint import linked_list_midpoint
from codinginterviewprep.fastandslowpointers.linked_list_midpoint import LinkedListNode


class TestLinkedListMidpoint(unittest.TestCase):

    def test_odd_example(self):
        node5 = LinkedListNode(3, None)
        node4 = LinkedListNode(7, node5)
        node3 = LinkedListNode(4, node4)
        node2 = LinkedListNode(2, node3)
        node1 = LinkedListNode(1, node2)

        result = linked_list_midpoint(node1)
        self.assertEqual(4, result)

    def test_even_example(self):
        node4 = LinkedListNode(7, None)
        node3 = LinkedListNode(6, node4)
        node2 = LinkedListNode(2, node3)
        node1 = LinkedListNode(1, node2)

        result = linked_list_midpoint(node1)
        self.assertEqual(6, result)

    def test_only_onenode(self):
        node1 = LinkedListNode(1, None)

        result = linked_list_midpoint(node1)
        self.assertEqual(1, result)

    def test_only_twonode(self):
        node2 = LinkedListNode(7, None)
        node1 = LinkedListNode(1, node2)

        result = linked_list_midpoint(node1)
        self.assertEqual(7, result)
