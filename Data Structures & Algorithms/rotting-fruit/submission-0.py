from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q_rotten = deque()
        fresh = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q_rotten.append((i,j,0))
                elif grid[i][j] == 1:
                    fresh += 1
        
        # Now i have a queue of all the original rotten and total fresh at hand

        # do bfs
        dir_pos = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        ans = 0
        while q_rotten:
            node = q_rotten.popleft()
            i = node[0]
            j = node[1]
            t = node[2]
            ans = max(t,ans)
            
            #  check all direction
            for dr, dc in dir_pos:
                row = i+ dr
                col = j + dc
                if (row in range(len(grid))) and (col in range(len(grid[0])) and grid[row][col] == 1):
                    fresh -= 1
                    grid[row][col] = 2
                    q_rotten.append((row,col,t+1))

        if fresh == 0:
            return ans
        
        return -1

                    