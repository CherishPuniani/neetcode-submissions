class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans, temp = [], []
        tot = len(candidates)
        candidates.sort()

        def help(i, target):
            if target <= 0:
                if target == 0:
                    ans.append(temp.copy())
                return
            if i == tot:
                return
            
            # pick
            temp.append(candidates[i])
            help(i+1, target-candidates[i])
            temp.pop()


            while i<len(candidates)-1 and candidates[i] == candidates[i+1]:
                i += 1
            
            # don't pick
            help(i+1, target)

        help(0, target)
        return ans