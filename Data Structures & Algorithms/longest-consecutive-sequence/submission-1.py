# To reduce Tc we can solve this without sorting so taking out the nLogn step
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numS = set(nums)
        ans = 0
        for num in nums:
            if num-1 not in numS:
                l = 1
                while num+1 in numS:
                    l += 1
                    num += 1
                ans = max(ans,l)
            else:
                continue
        return ans
        