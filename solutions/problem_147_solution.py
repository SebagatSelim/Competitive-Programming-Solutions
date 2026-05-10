# Problem 147: Valid Anagram
# Description: Check if string t is an anagram of string s.
# Time Complexity: O(N) | Space Complexity: O(1)
# Language: Python 3

def solve(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
    for char in t:
        if char not in count or count[char] == 0:
            return False
        count[char] -= 1
    return True
