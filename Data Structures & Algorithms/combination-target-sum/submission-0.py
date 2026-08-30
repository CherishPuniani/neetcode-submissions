class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans, temp = [], []
        tot = len(nums)

        def help(i, target):
            # base case
            if target <= 0:
                if target == 0: 
                    ans.append(temp[:])
                return
            if i == tot:
                return

            # don't pick
            help(i+1, target)
            #  pick
            temp.append(nums[i])
            help(i, target-nums[i])
            target += temp.pop()
        
        help(0, target)
        return ans