class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return nums[0]
        if n==2:
            return max(nums[0],nums[1])

        def help(arr):
            size = len(arr)
            # dp = [0] * size
            prev = arr[0]
            curr = max(arr[0], arr[1])

            for i in range(2,size):
                prev,curr = curr, max(arr[i]+prev,curr)
                # dp[i] = max(dp[i-1],arr[i]+dp[i-2])
            
            return curr

        return max(help(nums[1:]),help(nums[:-1]))
    