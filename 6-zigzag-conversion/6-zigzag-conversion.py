class Solution:
    def convert(self, s: str, numRows: int) -> str:
        grid = [[""] * len(s) for _ in range(numRows)]
        if (numRows == 1):
            return s
        
        row_idx = col_idx = 0
        direction = 1
        for i in range(len(s)):
            grid[row_idx][col_idx] = s[i]
            
            if (row_idx == numRows-1):
                direction = -1
            if (row_idx == 0):
                direction = 1
            
            if (direction == -1):
                col_idx += 1
                
            row_idx += direction
        
        return "".join(["".join(i) for i in grid])