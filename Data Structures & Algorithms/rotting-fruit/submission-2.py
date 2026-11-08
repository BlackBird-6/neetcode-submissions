class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        minute = 0
        ROWS, COLS = len(grid), len(grid[0])
        adjs = [[0,1],[0,-1],[1,0],[-1,0]]
        q = deque()

        fresh_count = 0

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    fresh_count += 1
                if grid[i][j] == 2:
                    q.append((i, j))
        
        while fresh_count > 0 and q:
            for _ in range(len(q)):
                i, j = q.popleft()
                
                for di, dj in adjs:
                    ni, nj = i+di, j+dj

                    if ni < 0 or ni >= ROWS or nj < 0 or nj >= COLS:
                        continue
                    if grid[ni][nj] == 1:
                        grid[ni][nj] = 2
                        fresh_count -= 1
                        q.append((ni, nj))

            minute += 1
        
        if fresh_count:
            return -1

        return minute

        