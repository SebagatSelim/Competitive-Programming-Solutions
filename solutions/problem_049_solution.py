# Problem 049: Climbing Stairs (Dynamic Programming)
# Description: Calculate how many distinct ways you can climb n stairs.
# Time Complexity: O(N) | Space Complexity: O(1)
# Language: Python 3

def solve(n: int) -> int:
    if n <= 2:
        return n
    first, second = 1, 2
    for _ in range(3, n + 1):
        first, second = second, first + second
    return second
