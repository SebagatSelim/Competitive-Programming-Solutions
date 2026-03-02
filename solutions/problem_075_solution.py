# Problem 075: Missing Number
# Description: Find the missing number in an array containing numbers 0 to n.
# Time Complexity: O(N) | Space Complexity: O(1)
# Language: Python 3

def solve(nums: list[int]) -> int:
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    return expected_sum - sum(nums)
