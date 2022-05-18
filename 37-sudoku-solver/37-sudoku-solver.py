class Solution:
    def check(self, x, y, num):
        for yy in range(9):
            if (self.board[yy][x] == num):
                return False

        for xx in range(9):
            if (self.board[y][xx] == num):
                return False

        for xx in range(x - x%3, x - x%3 + 3):
            for yy in range(y - y%3, y - y%3 + 3):
                if (self.board[yy][xx] == num):
                    return False

        return True

    def checkDot(self):
        for x in range(9):
            for y in range(9):
                if (self.board[y][x] == '.'):
                    return x, y
        return -1, -1

    def sol(self):
        x, y = self.checkDot()
        if (x == -1 and y == -1):
            return True

        for num in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            if (self.check(x, y, num)):
                self.board[y][x] = num
                if( self.sol() ):
                    return True
                self.board[y][x] = '.'
        return False
    
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.sol()