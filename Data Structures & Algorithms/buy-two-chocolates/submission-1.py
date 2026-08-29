class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        # input: prices integer array
        # money: single integer money (initial amount of money)
        # find min price to still have money left 
        # output: return money left or money
        sorted_p = sorted(prices)
        min_s = (sorted_p[0] + sorted_p[1])
        if money - min_s < 0:
            return money
        else:
            return money - min_s

        
        