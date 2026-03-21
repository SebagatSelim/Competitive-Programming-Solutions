# Problem 098: Symmetric Tree
# Description: Check whether a binary tree is a mirror of itself.
# Time Complexity: O(N) | Space Complexity: O(H)
# Language: Python 3

def isMirror(t1, t2):
    if not t1 and not t2: return True
    if not t1 or not t2: return False
    return (t1.val == t2.val) and isMirror(t1.right, t2.left) and isMirror(t1.left, t2.right)

def solve(root) -> bool:
    return isMirror(root, root)
