class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights) # y
        n = len(heights[0]) # x
        
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        
        pac_s = set()
        atl_s = set()
        
        def bfs(y, x, s):
            s.add( (y, x) )
            for i in range(4):
                x2 = x+dx[i]
                y2 = y+dy[i]
                if ((y2, x2) not in s and
                    x2 >= 0 and
                    y2 >= 0 and
                    x2 < n and
                    y2 < m and
                    heights[y][x] <= heights[y2][x2]):
                    bfs(y2, x2, s)
                
        for i in range(m):
            bfs(i, 0, pac_s)
            bfs(i, n-1, atl_s)
            
        for j in range(n):
            bfs(0, j, pac_s)
            bfs(m-1, j, atl_s)
            
        return pac_s.intersection(atl_s)
                
        