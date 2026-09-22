class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(cost)
        left = [0] * n
        tot = 0
        for i in range(n):
            left[i] = gas[i] - cost[i]
            tot += left[i]

        if tot < 0:
            return -1

        g = 0
        ans = 0
        t = 0
        while t < n:
            g += left[t]
            t+=1
            if g <= 0:
                g = 0
                ans = t%n

        return ans
            
        
