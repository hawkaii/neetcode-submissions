class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def isIsland(grid, pos):
            grid[pos[0]][pos[1]] = "#"
            dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for dir in dirs:
                x = pos[0] + dir[0]
                y = pos[1] + dir[1]
                if x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0]):
                    if grid[x][y] == "1":
                        grid[x][y] = "#"
                        isIsland(grid, (x, y))
            return grid

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    count += 1
                    grid = isIsland(grid, (i, j))
        return count
