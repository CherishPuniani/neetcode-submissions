class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        max_area = 0

        while i < j:
            hl, hr = heights[i], heights[j]
            ar = min(hl, hr) * (j - i)
            max_area = max(max_area, ar)

            if hl <= hr:
                while i < j and heights[i] <= hl:
                    i += 1
            else:
                while i < j and heights[j] <= hr:
                    j -= 1

        return max_area