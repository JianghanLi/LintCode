import sys
sys.setrecursionlimit(10002)

class Solution(object):
    """
    @param n: a positive integer
    @return: An integer
    """
    memo = {0: 0}

    def numSquares(self, n):
        if n in self.memo:
            return self.memo[n]
        self.memo[n] = float('inf')
        i = 1
        while i * i <= n:
            self.memo[n] = min(self.memo[n], self.numSquares(n - i * i) + 1)
            i += 1
        return self.memo[n]
