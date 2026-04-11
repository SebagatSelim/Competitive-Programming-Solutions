# Problem 113: Single Number
# Description: Find the element that appears once where others appear twice using XOR.
# Time Complexity: O(N) | Space Complexity: O(1)
# Language: Python 3

def solve(nums: list[int]) -> int:
    res = 0
    for num in nums:
        res ^= num
    return res
