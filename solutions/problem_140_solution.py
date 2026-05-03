# Problem 140: Intersection of Two Arrays
# Description: Return an array of elements common to both arrays (unique).
# Time Complexity: O(N + M) | Space Complexity: O(N + M)
# Language: Python 3

def solve(nums1: list[int], nums2: list[int]) -> list[int]:
    return list(set(nums1) & set(nums2))
