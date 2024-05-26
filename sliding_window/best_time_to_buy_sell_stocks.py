# 121. Best Time to Buy and Sell Stock
# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

def max_profit(prices):
    current_buy_day = 0
    max_profit = 0

    for day in range(1, len(prices)):
        if prices[day] < prices[current_buy_day]:
            current_buy_day = day
        current_profit = prices[day] - prices[current_buy_day]
        max_profit = max(max_profit, current_profit)
    return max_profit


prices1 = [7,1,5,3,6,4]
prices2 = [7,6,4,3,1]
prices3 = [1,2]
prices4 = [2,1,2,1,0,1,2]
prices5 = [3,3,5,0,0,3,1,4]

print(max_profit(prices2))