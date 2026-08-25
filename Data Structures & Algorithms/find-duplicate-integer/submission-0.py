class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # hmap = defaultdict(int)
        sett = set()

        for x in nums:
            if x in sett:
                return x
            else:
                sett.add(x)
        
        return 0
        
        
