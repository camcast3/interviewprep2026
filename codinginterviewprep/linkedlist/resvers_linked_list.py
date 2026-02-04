class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def reverse_linked_list(head: ListNode) -> ListNode:
    """
    Reverse a linked list by iterating through and flipping pointers.

    Time Complexity: O(n) - visit each node once
    Space Complexity: O(1) - only use pointers, no extra data structures
    """
    current_node, previous_node = head, None
    reversed_head = None

    print("Starting reverse...")
    print(
        f"Initial - current: {current_node.value if current_node else None}, previous: {previous_node}")

    step = 0
    while current_node is not None:
        step += 1
        print(f"\n--- Step {step} ---")
        print(f"Current node: {current_node.value}")

        # Save next node before we change the pointer
        tmp = current_node.next
        print(f"Saved tmp: {tmp.value if tmp else None}")

        # Reverse the pointer
        current_node.next = previous_node
        print(
            f"Flipped: current({current_node.value}).next now points to previous({previous_node.value if previous_node else 'None'})")

        # Move pointers forward
        reversed_head = current_node
        previous_node = current_node
        current_node = tmp
        print(
            f"After: current -> {current_node.value if current_node else None}, previous -> {previous_node.value}")

    print(f"\n✓ Reversal complete!")
    print(f"New head: {reversed_head.value if reversed_head else None}")
    return reversed_head


def display_linked_list(head: ListNode) -> str:
    """
    Display the linked list as a string.

    Time Complexity: O(n) - visit each node once
    Space Complexity: O(n) - store string representation
    """
    result = []
    current = head

    while current is not None:
        result.append(str(current.value))
        current = current.next

    return " -> ".join(result) + " -> None"


# Test it
if __name__ == "__main__":
    # Create: 1 -> 2 -> 3 -> None
    node3 = ListNode(3)
    node2 = ListNode(2, node3)
    node1 = ListNode(1, node2)

    print("Original list: 1 -> 2 -> 3 -> None\n")
    reversed = reverse_linked_list(node1)
    print(display_linked_list(reversed))
