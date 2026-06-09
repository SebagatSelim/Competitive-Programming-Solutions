# Problem 177: Majority Element (Boyer-Moore Voting)
# Description: Find the element that appears more than n/2 times.
# Time Complexity: O(N) | Space Complexity: O(1)
# Language: Python 3

def solve(nums: list[int]) -> int:
    candidate = None
    count = 0
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    return candidate
