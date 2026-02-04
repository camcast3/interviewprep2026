class LinkedListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def linked_list_midpoint_works_but_complicated(head: LinkedListNode) -> int:
    # Time complexity: O(length + length // 2)

    find_middle_pointer = find_end_pointer = head
    count = 1
    visited_nodes = 1

    while find_end_pointer:
        find_end_pointer = find_end_pointer.next
        count += 1

    if count % 2 == 0:
        middle_node = count // 2
    else:
        middle_node = (count // 2) + 1

    while visited_nodes < middle_node:
        find_middle_pointer = find_middle_pointer.next
        visited_nodes += 1

    return find_middle_pointer.value


def linked_list_midpoint(head: LinkedListNode) -> int:
    """
    Find the midpoint of a linked list using fast and slow pointers.

    For even length: returns the upper middle node
    For odd length: returns the middle node

    Time Complexity: O(n) - single pass
    Space Complexity: O(1) - only pointers
    """
    slow = fast = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    if fast is None:
        print(f"Even path is {slow.value}")
    elif fast.next is None:
        print(f"Odd path is {slow.value}")

    return slow.value
