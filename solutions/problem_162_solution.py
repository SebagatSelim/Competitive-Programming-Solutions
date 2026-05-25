# Problem 162: Valid Parentheses
# Description: Determine if the input string containing brackets is valid.
# Time Complexity: O(N) | Space Complexity: O(N)
# Language: Python 3

def solve(s: str) -> bool:
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char in mapping:
            top = stack.pop() if stack else '#'
            if mapping[char] != top:
                return False
        else:
            stack.append(char)
    return not stack
