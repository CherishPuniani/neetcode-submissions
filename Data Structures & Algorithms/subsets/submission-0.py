class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans, temp = [], []
        total = len(nums)

        def help(i):
            if i == total:
                ans.append(temp[:])
                return

            # num not chosen
            help(i+1)

            # num chosen
            temp.append(nums[i])
            help(i+1)
            temp.pop()

        help(0)
        return ans