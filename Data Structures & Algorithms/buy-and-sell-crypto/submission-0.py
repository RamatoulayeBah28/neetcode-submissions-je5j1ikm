class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # # Initialize maxprofit
        # maxP = 0
        # # iterate. through the list
        # for i in range(len(prices)):
        #     for j in range(i+ 1, len(prices)):
        #         maxP = max(prices[j] - prices[i], maxP)
                    
        # return maxP

        maxP = 0
        min_price = float("inf")
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            if prices[i] - min_price > maxP:
                maxP = prices[i] - min_price
        return maxP
        




