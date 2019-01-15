"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

class Solution:
    """
    @param l: The length of the matrix
    @param w: The width of the matrix
    @param points: three points
    @return: The sum of the paths sum
    """
    def calculationTheSumOfPath(self, l, w, points):
        points = sorted([[1, 1]] + [[p.x, p.y] for p in points] + [[l, w]])
        # points = sorted([[1, 1]] + points + [[l, w]])
        res = []
        def A(x, y):
            res = 1
            for i in range(1, x + 1): res *= i
            for i in range(1, y + 1): res /= i
            for i in range(1, x - y + 1): res /= i
            return res
        for p1, p2 in zip(points, points[1:]):
            y = p2[1] - p1[1]
            x = p2[0] - p1[0]
            res.append(A(x + y, x) % 1000000007)
        res2 = 1
        for i in res:
            res2 *= i
        return res2 % 1000000007


############ test cases ###########
s = Solution()
print s.calculationTheSumOfPath(4, 4, [[1, 1], [2, 2], [3, 3]])
print s.calculationTheSumOfPath(92, 100, [[45, 48], [15, 29], [92, 100]])  # 4282067

# https://www.lintcode.com/problem/calculation-the-sum-of-path/description
