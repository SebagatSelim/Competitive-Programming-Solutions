# Problem 188: Linked List Cycle (Floyd's Algorithm)
# Description: Detect if a linked list contains a cycle using fast and slow pointers.
# Time Complexity: O(N) | Space Complexity: O(1)
# Language: Python 3

def solve(head) -> bool:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
