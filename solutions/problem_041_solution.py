# Problem 041: Two Sum
# Description: Find two numbers in an array that add up to a target value.
# Time Complexity: O(N) | Space Complexity: O(N)
# Language: Python 3

def solve(nums: list[int], target: int) -> list[int]:
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i
    return []
