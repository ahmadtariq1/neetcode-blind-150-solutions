class Solution:
    def maxArea(self, heights: List[int]) -> int:
        

        max = 0
        size = len(heights)
        i = 0
        j = size - 1
        while i < j:

            area = min(heights[i] , heights[j]) * (j - i)
            if(max < area):
                max = area
            if(heights[i] < heights[j]):
                i += 1
            else:
                j -= 1
            
            
        return max
