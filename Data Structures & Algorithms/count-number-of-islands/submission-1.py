class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= ROWS or j < 0 or j >= COLS:
                return
            if grid[i][j] != "1":
                return
            
            grid[i][j] = "0"
            adjs = [[1,0],[-1,0],[0,1],[0,-1]]
            for dx, dy in adjs:
                dfs(i+dx, j+dy)

        res = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    res += 1
                    dfs(i,j)
            
        return res
        