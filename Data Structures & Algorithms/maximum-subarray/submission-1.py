class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        tot = nums[0]
        currMax = nums[0]

        for i in range(1,len(nums)):
            tot = max(nums[i], tot+nums[i])
            currMax = max(currMax,tot)
        
        return currMax