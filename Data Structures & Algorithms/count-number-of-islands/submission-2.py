class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [(-1,0), (0,1), (1,0), (0,-1)]

        R = len(grid)
        C = len(grid[0])
        count = 0

        # seen = set()
        

        def bfs(i,j):
            q = deque()
            q.append([i,j])
            # seen.add((i,j))
            
            while q:
                row,col = q.popleft()

                for dr,dc in dirs:
                    r = row+dr
                    c = col+dc

                    if (0<=r < R) and (0 <= c < C) and grid[r][c] == "1":
                        # seen.add((r,c))
                        q.append([r,c])
                        grid[r][c] = "0"
        
        for i in range(R):
            for j in range(C):
                if grid[i][j] == "1":
                    count+=1
                    bfs(i,j)

        return count
                

