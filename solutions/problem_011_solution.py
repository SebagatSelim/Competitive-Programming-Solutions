# Problem 011: Invert Binary Tree
# Description: Invert a binary tree (mirror image).
# Time Complexity: O(N) | Space Complexity: O(H)
# Language: Python 3

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode) -> TreeNode:
    if not root:
        return None
    root.left, root.right = solve(root.right), solve(root.left)
    return root
