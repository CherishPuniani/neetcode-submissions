class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj = defaultdict(list)
        for s,e,t in times:
            adj[s].append([t,e])
        
        t = [float('inf')] * n
        t[k-1] = 0

        heap = [[0,k]]
        
        while heap:
            time,loc = heapq.heappop(heap)

            if time > t[loc-1]:
                continue
            
            

            for y in adj[loc]:
                if time+y[0] < t[y[1]-1]:
                    t[y[1]-1] = time + y[0]
                    heapq.heappush(heap,[y[0]+time,y[1]])

        maxt = 0
        for l in t:
            if l == float('inf'):
                return -1
            maxt = max(l,maxt)

        return maxt
            
        
