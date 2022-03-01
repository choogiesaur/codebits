# For list of stock prices where list[i] = stock price for the ith day,
# Find the maximum profit you can make by buying one day, selling on a later day
# This is a one pass solution.
# Hint: Observe maximal distance from a valley to a later peak.

prices = [7,1,5,3,6,4]

def maxProfit(self, prices: List[int]) -> int:

    # Keep track of the smallest price seen so far
    # Max value from description is 10 ^ 4
    # Could use sys.maxint
    min_encountered = (10 ** 4) + 1

    # Keep track of the max profit seen for any window so far
    max_profit = 0

    for i in range(len(prices)):
      
        # If this is the lowest price we've seen so far, make note of it
        if prices[i] < min_encountered:
            min_encountered = prices[i]
            
        # If profit for this window is greater than anything we've seen, make note of it
        else:
            if prices[i] - min_encountered > max_profit:
                max_profit = prices[i] - min_encountered

    return max_profit

# Alt solution processing array in reverse
def maxProfit(self, prices: List[int]) -> int:

    min_price = 10001
    max_price = 0
    max_profit = 0

    for curr_price in reversed(prices):

        # Can always update with newly found min price
        min_price = min(min_price, curr_price)

        # If you found a new max, it occurred before the existing min, so...
        # Take note of current profit, update max profit if new one is better
        # Reset min to current price
        if curr_price > max_price:
            max_profit = max(max_profit, max_price - min_price)
            max_price = curr_price
            min_price = curr_price

    return max(max_profit, max_price - min_price)
