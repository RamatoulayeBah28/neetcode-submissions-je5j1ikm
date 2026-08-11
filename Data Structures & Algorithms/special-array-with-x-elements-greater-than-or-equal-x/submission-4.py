class Solution:
    def specialArray(self, nums: List[int]) -> int:

        s_nums = sorted(nums)
        for x in range(0, len(s_nums)+1):
            count = 0
            l, r = 0, len(s_nums) - 1
            while l <= r:
                if s_nums[l] >= x:
                    count += r-l + 1
                    break
                l+=1
            if count == x:
                return count
        return -1 

                


        