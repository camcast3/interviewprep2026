import unittest
from codinginterviewprep.fastandslowpointers.linked_list_loop import is_linked_list_loop
from codinginterviewprep.fastandslowpointers.linked_list_loop import LinkedListNodes


class TestLinkedListLoop(unittest.TestCase):

    def test_nonloop_example(self):
        """Test detection of linked list WITHOUT a loop"""
        node5 = LinkedListNodes(5, None)
        node4 = LinkedListNodes(4, node5)
        node3 = LinkedListNodes(3, node4)
        node2 = LinkedListNodes(2, node3)
        node1 = LinkedListNodes(1, node2)
        node0 = LinkedListNodes(0, node1)

        result = is_linked_list_loop(node0)
        self.assertFalse(
            result,
            "Expected False for linear list (0 -> 1 -> 2 -> 3 -> 4 -> 5 -> None), "
            f"but got {result}")

    def test_loop_example(self):
        """Test detection of linked list WITH a loop"""
        node5 = LinkedListNodes(5, None)
        node4 = LinkedListNodes(4, node5)
        node3 = LinkedListNodes(3, node4)
        node2 = LinkedListNodes(2, node3)
        node1 = LinkedListNodes(1, node2)
        node0 = LinkedListNodes(0, node1)
        # Create loop: 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 2 (cycle)
        node5.next = node2

        result = is_linked_list_loop(node0)
        self.assertTrue(
            result,
            "Expected True for looped list (node5.next points back to node2), "
            f"but got {result}")
