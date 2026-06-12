class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # set l and r pointers
        # set mid pointer
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l+r)// 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid -1
            else:
                return mid
                
        return -1
 

