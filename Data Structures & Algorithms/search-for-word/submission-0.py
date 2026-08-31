class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # ans = False
        # rows = len(board)
        # cols = len(board[0])

        def help(i,j,idx) -> bool:
            # base condition
            if idx == len(word):
                return True
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[idx]:
                return False

            # # check left
            # if j > 0:
            #     return help(i,j-1,idx+1)
            # # check right
            # if j < len(board[0])-1:
            #     return help(i,j+1,idx+1)
            # # check bottom
            # if i < len(board)-1:
            #     return help(i+1,j,idx+1)
            # # check top
            # if i > 0:
            #     return help(i-1,j,idx+1)

            # Mark cell as visited
            temp = board[i][j]
            board[i][j] = "$"

            found = (help(i+1,j,idx+1) or help(i,j+1,idx+1) or help(i-1,j,idx+1) or help(i,j-1,idx+1))

            board[i][j] = temp
            return found

        for r in range(len(board)):
            for c in range(len(board[0])):
                if help(r,c,0):
                    return True

        return False
