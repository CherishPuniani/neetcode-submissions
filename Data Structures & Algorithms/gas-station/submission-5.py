class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0
        curr = 0
        ans = 0

        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total += diff
            curr += diff

            if curr < 0:
                curr = 0
                ans = i + 1

        if total < 0:
            return -1

        return ans