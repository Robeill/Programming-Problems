class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = []
        for i in range(m - 2):
            row = []
            for j in range(n - 2):
                res = 0
                for x in range(i, i + 3):
                    for y in range(j, j + 3):
                        res = max(res, grid[x][y])
                row.append(res)
            ans.append(row)
        return ans