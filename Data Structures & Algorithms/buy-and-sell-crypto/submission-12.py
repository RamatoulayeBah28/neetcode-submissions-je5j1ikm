# [5, 1, 5, 6, 7, 1, 10] profit = 1-10 prices[1] - prices[6] = 9
# l = 1 r = 5 max = 4
# l = 1 r = 6 6-1 5
# l = 1 r = 7 6
# 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        l = 0
        r = l + 1
        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
            max_profit = max(max_profit, prices[r] - prices[l])
            r += 1
        return max_profit
# [3,2,6,1,4]
# while r number is lower than l pointer best buying day is number at r l = r r+=1
#best profit is prices[r] - prices[l] r+=1
# 
# 
# 
        