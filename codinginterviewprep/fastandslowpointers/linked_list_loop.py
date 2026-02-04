class LinkedListNodes:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def is_linked_list_loop(head: LinkedListNodes) -> bool:

    slow_pointer = fast_pointer = head

    while fast_pointer and fast_pointer.next:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next

        if slow_pointer == fast_pointer:
            return True

    return False
