class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for arr in matrix:
            if self.binary_search(arr, target) == True:
                return True
        return False
    
    def binary_search(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l+r) // 2
            if target < nums[mid]:
                r = mid - 1
            elif target > nums[mid]:
                l = mid + 1
            else:
                return True
        return False
        