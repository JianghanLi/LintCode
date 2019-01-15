class Solution:
    """
    @param height: the Cable car station height
    @return: the longest time that he can ride
    """
    def cableCarRide(self, A):
        R, C = len(A), len(A[0])
        index = {}
        for r, row in enumerate(A):
            for c, val in enumerate(row):
                index[val] = r, c

        def neighbors(r, c):
            for dr in xrange(-1, 2):
                for dc in xrange(-1, 2):
                    if dr or dc:
                        if 0 <= r + dr < R and 0 <= c + dc < C:
                            yield r + dr, c + dc

        dp = [[1] * C for _ in A]
        for v, (r, c) in sorted(index.items(), reverse=True):
            for nr, nc in neighbors(r, c):
                if A[nr][nc] < v:
                    dp[nr][nc] = max(dp[nr][nc], dp[r][c] + 1)

        return max(max(row) for row in dp)
