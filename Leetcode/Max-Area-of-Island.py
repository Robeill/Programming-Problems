class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def is_out_of_bounds(r, c):
            return r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0])

        def dfs(r, c):
            if is_out_of_bounds(r, c) or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            area = 1
            for dr, dc in move:
                area += dfs(r + dr, c + dc)
            return area

        move = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        max_area = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c))
        
        return max_area
