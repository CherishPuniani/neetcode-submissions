class Solution:
    def calcHours(self,piles: List[int], k=1) -> int:
        hours = 0
        for x in piles:
            hours -= (-x//k)
        return hours

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxEl = 0
        for x in piles:
            maxEl = max(maxEl, x)
        l = 1
        r = maxEl
        
        while(l < r):
            mid = l + (r-l)//2
            if self.calcHours(piles,mid) > h:
                l = mid + 1
            else:
                r = mid
        
        return r
        
