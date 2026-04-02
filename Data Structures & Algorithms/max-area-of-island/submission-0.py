class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        max_area = 0

        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == 1:
                    stack = [(r, c)]
                    grid[r][c] = 0
                    area = 0

                    while stack:
                        x, y = stack.pop()
                        area += 1

                        if x+1 < rows and grid[x+1][y] == 1:
                            stack.append((x+1, y))
                            grid[x+1][y] = 0

                        if x-1 >= 0 and grid[x-1][y] == 1:
                            stack.append((x-1, y))
                            grid[x-1][y] = 0

                        if y+1 < cols and grid[x][y+1] == 1:
                            stack.append((x, y+1))
                            grid[x][y+1] = 0

                        if y-1 >= 0 and grid[x][y-1] == 1:
                            stack.append((x, y-1))
                            grid[x][y-1] = 0

                    max_area = max(max_area, area)

        return max_area