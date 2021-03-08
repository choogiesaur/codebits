# For list of stock prices where list[i] = stock price for the ith day,
# Find the maximum profit you can make by buying one day, selling on a later day

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
