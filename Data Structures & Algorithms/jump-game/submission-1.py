class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False]* n
        dp[0] = True

        for i in range(n):
            if dp[i] == True:
                t = 0
                while t<nums[i] and i+t+1 < n:
                    dp[i+t+1] = True
                    t+=1

        return dp[n-1]