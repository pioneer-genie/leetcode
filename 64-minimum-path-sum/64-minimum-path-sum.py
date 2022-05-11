class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        lx = len(grid[0])
        ly = len(grid)
        grid_s = [[987654321 for _ in range(lx)] for j in range(ly)]
        grid_s[0][0] = grid[0][0]
        
        def dfs(x, y):
            if (y < ly-1 and grid_s[y][x] + grid[y+1][x] < grid_s[y+1][x]):
                grid_s[y+1][x] = grid_s[y][x] + grid[y+1][x]
                dfs(x, y+1)
            if (x < lx-1 and grid_s[y][x] + grid[y][x+1] < grid_s[y][x+1]):
                grid_s[y][x+1] = grid_s[y][x] + grid[y][x+1]
                dfs(x+1, y)
        
        dfs(0, 0)
        
        return grid_s[ly-1][lx-1]
            