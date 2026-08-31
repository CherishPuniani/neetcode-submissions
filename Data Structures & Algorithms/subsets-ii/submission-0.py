class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans, temp = [], []
        tot = len(nums)
        nums.sort()

        def help(i):
            if i == len(nums):
                ans.append(temp[:])
                return

            # pick
            temp.append(nums[i])
            help(i+1)
            temp.pop()

            while i<len(nums)-1 and nums[i] == nums[i+1]:
                i += 1

            # don't pick
            help(i+1)


        help(0)
        return ans

            