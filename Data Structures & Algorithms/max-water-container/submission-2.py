class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        max_area = 0
        
        while i < j:
            # Calculate current area
            ar = min(heights[i], heights[j]) * (j - i)
            max_area = max(max_area, ar)
            
            # Move the bottleneck pointer by 1 step
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
                
        return max_area