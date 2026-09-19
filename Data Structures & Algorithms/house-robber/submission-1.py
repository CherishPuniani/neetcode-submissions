class Solution:
    def rob(self, nums: List[int]) -> int:
        # top down approach

        n = len(nums)

        if n == 1:
            return nums[0]
        if n==2:
            return max(nums[0],nums[1])

        cache = {0: nums[0], 1: max(nums[0],nums[1])}

        def help(i):
            if i in cache:
                return cache[i]
            else:
                cache[i] = max(nums[i]+help(i-2), help(i-1))
                return cache[i]

        return help(n-1)
