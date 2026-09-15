class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, cost in flights:
            adj[u].append([cost, v])

        heap = [[0, src, k + 1]]
        
        # max_stops_left[node] tracks the most moves left when reaching `node`
        max_stops_left = [-1] * n
        
        while heap:
            cost, loc, stops_left = heapq.heappop(heap)

            if loc == dst:
                return cost

            # Prune if no moves left or if we previously reached `loc` with >= moves left
            if stops_left == 0 or max_stops_left[loc] >= stops_left:
                continue
            
            max_stops_left[loc] = stops_left
            
            for price, nxt in adj[loc]:
                heapq.heappush(heap, [cost + price, nxt, stops_left - 1])
        
        return -1