class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Understand
        # input: list of numbers sorted and target number
        # output: list of two indices
        # edge case: none since one valid answer and no duplicates

        # Match
        # hash map - dictionary
        # two sum problem 
        # 1-indexed

        # Plan 
        # brute force
        # for i in range len nums starting at 1
        # for i in range(len(numbers)):
        # # for j in range len nums i + 1
        #     for j in range(i+1, len(numbers)):
        # # if nums[i] + nums[j] == target:
        #         if numbers[i] + numbers[j] == target:
        #             return [i+1, j+1]
        # return []
        # binary search 
        l = 0
        r = len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            elif numbers[l]+ numbers[r] > target:
                r-=1
            else:
                l+=1


        