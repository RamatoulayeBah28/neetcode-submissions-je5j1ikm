class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # diff = target - num 
        # 7 - 3 so we return nums[i] and diff in the hashmap along its index
        # initialize a hashmap
        result = {}
        # for i in range len(nums):
        for i in range(len(nums)):
            diff = target - nums[i]
            
            if diff in result:
                return [result.get(diff), i]
            result[nums[i]] = i 
       