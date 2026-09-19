class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        cost.append(0)

        for i in range(3,len(cost)+1):
            i = -i
            cost[i] += min(cost[i+1],cost[i+2])
        
        return min(cost[0],cost[1])

