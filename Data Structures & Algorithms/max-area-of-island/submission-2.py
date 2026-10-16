class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])

        dirs = [(-1,0), (1,0), (0,-1), (0,1)]

        def dfs(i,j):

            if i not in range(0,R) or j not in range(0,C) or grid[i][j] == 0:
                return 0
            
            grid[i][j] = 0
            area = 1

            for dr,dc in dirs:
                r = i+dr
                c = j+dc
                # if grid[i][j] == 1:
                area += dfs(r,c)
            
            return area

            
        ans = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    ans = max(ans, dfs(i,j))
        
        return ans
