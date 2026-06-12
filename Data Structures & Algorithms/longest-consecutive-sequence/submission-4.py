# input: nums array 
# output: longest consecutive sequence

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        count = 0
        longest_s = 0
        set_nums = set(nums)
        for num in set_nums:
            # check if start of a sequence
            if num - 1 not in set_nums:
                count = 1
                while num + count in set_nums:
                    count+=1
                longest_s = max(longest_s, count)

        return longest_s
        
            



 
        