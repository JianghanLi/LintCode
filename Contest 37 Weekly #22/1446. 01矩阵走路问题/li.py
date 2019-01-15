class Solution:
    """
    @param grid: The gird
    @return: Return the steps you need at least
    """
    def getBestRoad(self, grid):
        n, m = len(grid), len(grid[0])
        bfs = [(0, 0)]
        d = [[0] * m for i in range(n)]
        d[0][0] = 1
        for x, y in bfs:
            for i, j in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                if 0 <= x + i < n and 0 <= y + j < m:
                    if grid[x + i][y + j] == 0 and d[x + i][y + j] == 0:
                        d[x + i][y + j] = d[x][y] + 1
                        bfs.append((x + i, y + j))
        # for i in grid: print i
        # print
        # for i in d: print i
        # print

        bfs = [(n - 1, m - 1)]
        d2 = [[0] * m for i in range(n)]
        d2[-1][-1] = 1
        for x, y in bfs:
            for i, j in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                if 0 <= x + i < n and 0 <= y + j < m:
                    if grid[x + i][y + j] == 0 and d2[x + i][y + j] == 0:
                        d2[x + i][y + j] = d2[x][y] + 1
                        bfs.append((x + i, y + j))

        # for i in d2: print i
        # print

        res = n * m * 2
        for x in range(n):
            for y in range(m):
                to1 = to2 = n * m * 2
                for i, j in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                    if 0 <= x + i < n and 0 <= y + j < m:
                        if 0 < d[x + i][y + j] < to1: to1 = d[x + i][y + j]
                        if 0 < d2[x + i][y + j] < to2: to2 = d2[x + i][y + j]
                res = min(res, to1 + to2)
        return res if res < m * n else -1


############ test cases ###########
s = Solution()
print s.getBestRoad(grid=[[0, 1, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 0], [1, 1, 1, 1, 0]])
print s.getBestRoad(grid=[[0, 1, 1], [1, 1, 0], [1, 1, 0]])


# https://www.lintcode.com/problem/01-matrix-walking-problem/description
