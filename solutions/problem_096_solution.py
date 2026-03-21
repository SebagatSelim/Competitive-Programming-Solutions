# Problem 096: First Unique Character in a String
# Description: Find the first non-repeating character in a string and return its index.
# Time Complexity: O(N) | Space Complexity: O(1)
# Language: Python 3

def solve(s: str) -> int:
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
    for i, char in enumerate(s):
        if count[char] == 1:
            return i
    return -1
