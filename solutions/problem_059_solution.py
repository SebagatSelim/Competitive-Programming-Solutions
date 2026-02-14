# Problem 059: Find Peak Element
# Description: Find a peak element in an array using Binary Search.
# Time Complexity: O(log N) | Space Complexity: O(1)
# Language: Python 3

def solve(nums: list[int]) -> int:
    low, high = 0, len(nums) - 1
    while low < high:
        mid = (low + high) // 2
        if nums[mid] > nums[mid + 1]:
            high = mid
        else:
            low = mid + 1
    return low
