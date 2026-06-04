class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Understand
        # input is a list of numbers (integers)
        # output is a list containing lists of triplets summing to 0 
        # edge case: if nums is empty return empty list

        # Match
        # brute force would be three for loops
        # sort the array + two pointers
        
        # initialize result = []
        result = []
        
        newNums = sorted(nums)
        
        
        for i, val in enumerate(newNums):
            if i > 0 and val == newNums[i-1]:
                continue
            l, r = i+1, len(newNums) -1
            while l < r:
                if val + newNums[l] + newNums[r] > 0:
                    r-=1
                elif val + newNums[l] + newNums[r] < 0:
                    l+=1
                else:
                    result.append([val, newNums[l], newNums[r]])
                    l+=1
                    while newNums[l] == newNums[l-1] and l <r:
                        l+=1

        return result


        
            
        