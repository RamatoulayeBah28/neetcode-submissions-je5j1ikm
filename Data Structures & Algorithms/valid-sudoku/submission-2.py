class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # define row col and grid hashset
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        # loop through every cell in the board
        for r in range(9):
            for c in range(9):
                # skip dots
                if board[r][c] == '.':
                    continue
                if board[r][c] in cols[c] or board[r][c] in rows[r] or board[r][c] in squares[(r//3, c//3)]:
                    return False
                # otherwise, add the digit to the hashset
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
        return True
                

        
        
            

        
                
        
        