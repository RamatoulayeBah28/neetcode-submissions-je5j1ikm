class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # set l and r pointers
        # set mid pointer
        l = 0
        r = len(nums) - 1
        mid = (l+r)// 2

        while l <= r:
            if nums[mid] == target:
                return nums.index(target)
            elif nums[mid] < target:
                l = mid + 1
                mid = (l+r)// 2
            elif nums[mid] > target:
                r = mid -1
                mid = (l+r)// 2
                
        return -1
 

