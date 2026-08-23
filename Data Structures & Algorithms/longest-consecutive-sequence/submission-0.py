class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxSize = 0
        nums.sort()
        num_set = set(nums)
        i = 0
        while i < len(nums):
            num = nums[i]
            l = 1
            while (num+1) in num_set:
                l += 1
                num += 1
            maxSize = max(l,maxSize)
            i += l
        return maxSize
                