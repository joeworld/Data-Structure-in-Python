"""
Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
Note that you cannot sell a stock before you buy one.
"""
A = [45, 24, 35, 31, 40]

# Brute force approach
# TC = O(N^2)
# SC = O(1)
def maximum_profit(stocks):
    max_profit = 0
    for i in range(len(stocks)-1): # Loop through
        for j in range(i+1, len(stocks)): # Walk through the loops gradually
            if stocks[j] - stocks[i] > max_profit: # Then compare
                max_profit = stocks[j] - stocks[i] # Assign max_profit

    return max_profit

# Proper Solution
def buy_nd_sell(stocks):
    max_profit = 0
    min_price = stocks[0]

    for price in stocks:
        min_price = min(min_price, price)
        compare_profit = price - min_price
        max_profit = max(max_profit, compare_profit)

    return max_profit

'''
min_price = 45
45
45-45 = 0
//0 nd min_price = 45

min_price = 24
24-24 = 0
//0 nd min_price = 24

min_price 24
35-24 = 11
//11 min_price = 24

min_price 24
40-24 = 16
//16 min_price = 24

min_price 24
59-24 = 35
//35 min_price = 24

'''

print(buy_nd_sell([45,24,35,40,59]))