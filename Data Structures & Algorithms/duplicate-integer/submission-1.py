class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        if nums:
            prev = nums[0]
            for x in nums[1:]:
                if x == prev:
                    return True
                prev = x
        return False