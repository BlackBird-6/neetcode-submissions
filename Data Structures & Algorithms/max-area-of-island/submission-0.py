class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        res = 0

        def dfs(i, j):
            if i < 0 or j < 0 or i >= ROWS or j >= COLS:
                return 0
            if grid[i][j] == 0:
                return 0
            
            grid[i][j] = 0
            return 1 + dfs(i+1, j) + dfs(i-1, j) + dfs(i, j+1) + dfs(i, j-1)

        for i in range(ROWS):
            for j in range(COLS):
                res = max(res, dfs(i, j))
        return res
        