class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # use max heap?
        for i in range(len(stones)):
            stones[i] = -stones[i]
        
        heapq.heapify(stones)
        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)

            z = -(y-x)
            if z != 0:
                heapq.heappush(stones,z)

        rest = len(stones)
        if rest == 1:
            return -stones[0]

        return 0
        
