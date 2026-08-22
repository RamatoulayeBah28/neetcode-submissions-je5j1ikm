class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        target = 0
        res = []
        new_n = sorted(nums)
        # [-4, -1, -1, 0, 1, 2]
        for i in range(len(new_n)):
            if i > 0 and new_n[i] == new_n[i-1]:
                continue
            l, r = i+1, len(new_n) - 1

            while l < r:
                three_sum = new_n[i] + new_n[l] + new_n[r]
                if three_sum > target:
                    r -= 1
                elif three_sum < target:
                    l+=1
                else:
                    res.append([new_n[i], new_n[l], new_n[r]])
                    l+=1
                    while new_n[l] == new_n[l-1] and l < r:
                        l+=1
        return res




        