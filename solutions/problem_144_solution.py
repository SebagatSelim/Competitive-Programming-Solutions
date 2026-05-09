# Problem 144: Maximum Subarray (Kadane's Algorithm)
# Description: Find the contiguous subarray with the largest sum.
# Time Complexity: O(N) | Space Complexity: O(1)
# Language: Python 3

def solve(nums: list[int]) -> int:
    max_so_far = nums[0]
    curr_max = nums[0]
    for i in range(1, len(nums)):
        curr_max = max(nums[i], curr_max + nums[i])
        max_so_far = max(max_so_far, curr_max)
    return max_so_far
