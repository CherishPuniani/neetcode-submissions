class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hset = set()
        for x in nums:
            if x in hset:
                return True
            else: 
                hset.add(x)
        return False        