# input: board 9 lists in a list containing an integer 1-9 or a . empty square
# output: a boolean true or false
# edge case: if board is empty we can just return True
# i represents the rows, j represents the columns
# are we guaranteed a value between 1-9?

# board[0][j] represents row 1
# board[1][j] represents row 2 
# board[2] represents row 3
# board[3] represents row 4
# board[4] represents row 5
# board[5] represents row 6
# board[6] represents row 7
# board[7] represents row 8
# board[8] represents row 9

# board[i][0] represents column 1
# board[i][1] represents column 2 
# board[2] represents column 3
# board[3] represents column 4
# board[4] represents column 5
# board[5] represents column 6
# board[6] represents column 7
# board[7] represents column 8
# board[8] represents column 9
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check each row so for lst in board:

        for row in range(9):
            seen = set()
            for col in range(9):
                if board[row][col] == ".":
                    continue
                if board[row][col] in seen:
                    return False
                seen.add(board[row][col])

        for col in range(9):
            seen = set()
            for i in range(9):
                if board[i][col] == ".":
                    continue
                if board[i][col] in seen:
                    return False
                seen.add(board[i][col])

        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        return True
        
            

        
                
        
        