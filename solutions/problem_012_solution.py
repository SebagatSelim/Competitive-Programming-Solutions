# Problem 012: Contains Duplicate
# Description: Return true if any value appears at least twice in the array.
# Time Complexity: O(N) | Space Complexity: O(N)
# Language: Python 3

def solve(nums: list[int]) -> bool:
    return len(nums) != len(set(nums))
