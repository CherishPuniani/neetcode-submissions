class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans, temp = [], []
        pickTracker = [False] * len(nums)

        def help():
            if len(temp) == len(nums):
                ans.append(temp[:])
                return

            for i in range(len(nums)):
                if not pickTracker[i]:
                    temp.append(nums[i])
                    pickTracker[i] = True
                    help()
                    temp.pop()
                    pickTracker[i] = False

        help()
        return ans

