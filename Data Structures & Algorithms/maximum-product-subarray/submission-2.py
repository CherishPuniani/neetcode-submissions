class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)

        currMax = 1
        currMin = 1
        ans = nums[0]

        for i in nums:
            currMax, currMin = max(i, i*currMax, i*currMin), min(i, i*currMax, i*currMin)
            ans = max(ans,currMax)

        return ans
        
