class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # trying to implement divide and conquer
        def dfs(l,r):
            if l > r:
                return -float('inf')
            
            rightSum = leftSum = currSum = 0
            m = (l+r) // 2

            #  get leftSum
            for i in range(m-1,l-1,-1):
                currSum += nums[i]
                leftSum = max(leftSum,currSum)
            
            currSum = 0
            for i in range(m+1,r+1):
                currSum += nums[i]
                rightSum = max(rightSum,currSum)

            return max(
                dfs(l,m-1), 
                dfs(m+1,r), 
                rightSum+leftSum+nums[m]
                )
        
        return dfs(0,len(nums)-1)