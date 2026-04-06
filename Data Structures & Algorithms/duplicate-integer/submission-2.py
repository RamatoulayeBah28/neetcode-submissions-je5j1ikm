class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # new_set = set(nums)
        # return len(new_set) != len(nums)
        new_set = set()
        for num in nums:
            if num in new_set:
                return True
            new_set.add(num)
        return False

        