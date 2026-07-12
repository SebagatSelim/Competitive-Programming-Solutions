# Problem 206: Reverse Linked List
# Description: Reverse a singly linked list iteratively.
# Time Complexity: O(N) | Space Complexity: O(1)
# Language: Python 3

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solve(head: ListNode) -> ListNode:
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev
