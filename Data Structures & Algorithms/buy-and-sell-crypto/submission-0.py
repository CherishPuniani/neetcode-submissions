class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        maxProf = 0
        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
            else:
                maxProf = max(maxProf, prices[r] - prices[l])
            r +=1

        return maxProf