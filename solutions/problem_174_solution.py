# Problem 174: Move Zeroes
# Description: Move all 0's to the end while maintaining relative order of non-zeroes.
# Time Complexity: O(N) | Space Complexity: O(1)
# Language: Python 3

def solve(nums: list[int]) -> None:
    left = 0
    for right in range(len(nums)):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
