# Understand
        # input: an array of integers
        # output: an array output containing all of nums except current num

# Match
    # brute force algo 


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # initialize output to be size of nums
        output = [1] * len(nums)
        # initialize a prefix var to 1
        prefix = 1
        # loop through nums left to right
        for i in range(len(nums)):
            # first index of the output is prefix
            output[i] = prefix
            # prefix updated value is curr val * num
            prefix *= nums[i]
        # initialize postfix
        postfix = 1
        # loop through nums right to left
        for i in range(len(nums)-1, -1, -1):
            # output at index i * postfix
            output[i] *= postfix
            # postfix * curr num
            postfix *= nums[i]
        return output


       