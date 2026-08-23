class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        col_map = defaultdict(set)
        row_map = defaultdict(set)
        box_map = defaultdict(set)

        for r in range(9):
            for c in range(9):
                el = board[r][c]
                if el == ".":
                    continue
                elif el in row_map[r]:
                    return False
                elif el in col_map[c]:
                    return False
                # check if it is present in the box
                elif el in box_map[(r//3 , c//3)]:
                    return False
                else:
                    row_map[r].add(el)
                    col_map[c].add(el)
                    box_map[(r//3, c//3)].add(el)
        
        return True
        
            