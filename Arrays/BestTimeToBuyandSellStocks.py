prices = [7,1,5,3,6,4]
max_profit = 0

#! This approach won't work for cases where minimum element is at the end of the array
#! because we can't sell before we buy

# i = prices.index(min(prices))  #* gives index of the minimum element of the array

# for j in range(i+1, len(prices)):
#     profit = prices[j] - prices[i]
#     if profit > max_profit:
#         max_profit = profit
#     else:
#         continue
# print(max_profit)

#! Approch 2 - Brute Force

# for i in range(len(prices)):
#     for j in range(i+1, len(prices)):
#         profit = prices[j]-prices[i]
#         if profit > max_profit:
#             max_profit = profit
#         else:
#             continue
# print(max_profit)

#! Approach 3 - Optimal Approach

prices = [7,1,5,3,6,4]
max_profit = 0

l = 0
r = 1

while r < len(prices):
    if prices[l] < prices[r]:
        profit = prices[r] - prices[l]
        if profit > max_profit:
            max_profit = profit
        r = r+1
    else:
        l = r
        r = r+1
        
print(max_profit)