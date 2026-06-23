class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Area = h * w --> 6 * 6 = 36
        # input list of integers
        # output max amount of water container can store
        maxArea = 0
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                if heights[j] < heights[i]:
                    maxArea = max(maxArea, heights[j] * (j-i))
                elif heights[j] >= heights[i]:
                    maxArea = max(maxArea, heights[i] * (j-i))

        return maxArea
                
        