class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])

        o_bor = []
        o_set = set()
        visited = set()
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    if i == 0 or j==0 or i==rows-1 or j==cols-1:
                        o_bor.append((i,j))
                    else:
                        o_set.add((i,j))
        
        # DFS or BFS from all these Os should be kept as is rest all X?
        def dfs(r,c):
            if (r,c) in visited:
                return
            if (r not in range(rows)) or (c not in range(cols)) or board[r][c] == "X":
                return

            if (r,c) in o_set:
                o_set.discard((r,c))

            visited.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        for p in o_bor:
            dfs(p[0],p[1])
        
        for q in o_set:
            board[q[0]][q[1]] = "X"
