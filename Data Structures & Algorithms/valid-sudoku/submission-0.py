class Solution:
    def checkRow(self, board: List[List[str]], row: int, col: int, target: str) -> bool:
        cols = len(board[0])
        for c in range(cols):
            if c != col and board[row][c] == target:
                return True
        return False

    def checkCol(self, board: List[List[str]], row: int, col: int, target: str) -> bool:
        rows = len(board)
        for r in range(rows):
            if r != row and board[r][col] == target:
                return True
        return False
    
    def checkSubgrid(self, board: List[List[str]], currRow: int, currCol: int, startRow: int, startCol: int, target: str) -> bool:
        for row in range(startRow, startRow + 3):
            for col in range(startCol, startCol + 3):
                if (row != currRow or col != currCol) and board[row][col] == target:
                    return True

        return False


    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = len(board), len(board[0])

        for row in range(rows):
            for col in range(cols):
                if board[row][col] != ".":
                    if self.checkRow(board, row, col, board[row][col]):
                        return False
                    if self.checkCol(board, row, col, board[row][col]):
                        return False
                    if self.checkSubgrid(board,row, col, row - (row%3), col - (col%3), board[row][col]):
                        return False

        return True
        