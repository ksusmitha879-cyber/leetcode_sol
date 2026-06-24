class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: 
            return 0

        n, m = len(grid), len(grid[0])

        def dfs(r, c):
            stack = [(r, c)]
            while stack:
                x, y = stack.pop()
                if 0 <= x < n and 0 <= y < m and grid[x][y] == '1':
                    grid[x][y] = '0'
                    stack.extend([(x+1,y), (x-1,y), (x,y+1), (x,y-1)])

        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i, j)
        return count
