"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: The intervals
    @param k: The k
    @return: The answer
    """
    def maximumLineCoverage(self, intervals, k):
        lines = [[i.start, i.end] for i in intervals]
        # lines = intervals
        lines.sort(key=lambda l: l[1])
        xmax = max(l[1] for l in lines)
        dp = [[0] * (k + 1) for _ in range(xmax + 1)]
        for s, e in lines:
            for i in range(s, e + 1):
                for j in range(1, k + 1):
                    dp[i][j] = max(dp[i][j], dp[s - 1][j - 1] + i - s + 1)
        return dp[xmax][k]

    def maximumLineCoverage(self, intervals, K):
        # x = max(i.end for i in intervals)
        x = max(i[1] for i in intervals)
        pre_index = [3000] * (x + 1)
        cur = 0
        # for start, end in sorted([[i.start, i.end] for i in intervals]):
        for start, end in sorted([i for i in intervals]):
            cur = max(cur, start)
            while cur <= end:
                pre_index[cur] = start
                cur += 1

        # dp[i][k] max coverage between [1, x] using k lines
        dp = [[0] * (K + 1) for _ in xrange(x + 1)]
        for i in range(1, x + 1):
            for k in range(1, K + 1):
                dp[i][k] = dp[i - 1][k]
                if pre_index[i] < 3000:
                    dp[i][k] = max(dp[i][k], dp[pre_index[i] - 1][k - 1] + i - pre_index[i] + 1)
        return dp[-1][k]

############ test case ###########
s = Solution()
print s.maximumLineCoverage([(1, 2), (2, 3), (3, 4)], 2)


# Total Runtime: 2521 ms
