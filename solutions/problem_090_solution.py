# Problem 090: Best Time to Buy and Sell Stock
# Description: Maximize profit by buying on one day and selling on another.
# Time Complexity: O(N) | Space Complexity: O(1)
# Language: Python 3

def solve(prices: list[int]) -> int:
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit
