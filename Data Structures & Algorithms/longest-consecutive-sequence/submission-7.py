class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        new_n = set(nums)
        longest = 0
        for num in new_n:
            if num - 1 not in new_n:
                length = 1
                while num + length in new_n:
                    length+=1
                longest = max(longest, length)
        return longest

        
       