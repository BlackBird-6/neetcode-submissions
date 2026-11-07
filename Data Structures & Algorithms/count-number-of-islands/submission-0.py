class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        seen = set()
        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= ROWS or j < 0 or j >= COLS:
                return False
            if (i, j) in seen:
                return False
            if grid[i][j] == "0":
                return False
            
            seen.add((i,j))

            adjs = [[1,0],[-1,0],[0,1],[0,-1]]
            for dx, dy in adjs:
                dfs(i+dx, j+dy)
            return True

        res = 0
        for i in range(ROWS):
            for j in range(COLS):
                res += dfs(i,j)
            
        return res
        