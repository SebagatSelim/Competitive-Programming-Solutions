# Problem 203: Merge Two Sorted Lists
# Description: Merge two sorted linked lists and return it as a new sorted list.
# Time Complexity: O(N + M) | Space Complexity: O(1)
# Language: Python 3

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solve(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode()
    tail = dummy
    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 or l2
    return dummy.next
