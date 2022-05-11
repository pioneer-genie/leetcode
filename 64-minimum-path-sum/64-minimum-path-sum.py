class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        lx = len(grid[0])
        ly = len(grid)
        
        for y in range(1, ly):
            grid[y][0] += grid[y-1][0]
        for x in range(1, lx):
            grid[0][x] += grid[0][x-1]
        
        for y in range(1, ly):
            for x in range(1, lx):
                grid[y][x] += min(grid[y][x-1], grid[y-1][x])
                
        return grid[ly-1][lx-1]
            