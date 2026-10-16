class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])

        dirs = [(-1,0), (1,0), (0,-1), (0,1)]

        def bfs(i,j):
            q = deque()
            q.append([i,j])
            size = 1
            grid[i][j] = 0

            while q:
                i,j = q.popleft()

                for dr,dc in dirs:
                    r = i+dr
                    c = j+dc

                    if r in range(0,R) and c in range(0,C) and grid[r][c] == 1:
                        size += 1
                        q.append([r,c])
                        grid[r][c] = 0
            
            return size

        ans = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    ans = max(ans, bfs(i,j))
        
        return ans

