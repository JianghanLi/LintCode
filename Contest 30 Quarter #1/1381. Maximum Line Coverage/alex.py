class Solution:
    """
    @param intervals: The intervals
    @param k: The k
    @return: The answer
    """
    def maximumLineCoverage(self, intervals, K):
        A = [(iv.start, iv.end) for iv in intervals]
        A.sort()

        if K == len(intervals):
            court = [0] * 2001
            for i, j in A:
                for k in xrange(i, j + 1):
                    court[k] = 1
            return sum(court)

        N = len(A)
        dp = [[0] * N for _ in xrange(K + 1)]
        ma = [0] * (K + 1)

        for i in xrange(N):
            dp[1][i] = A[i][1] - A[i][0] + 1
            ma[1] = max(ma[1], dp[1][i])

        NINF = float('-inf')
        for i in xrange(2, K + 1):
            for j in xrange(N):
                for k in xrange(j - 1, -1, -1):
                    if dp[i - 1][k] == NINF:
                        continue
                    if A[k][1] > A[j][1]:
                        dp[i][j] = NINF
                        break
                    if A[k][1] < A[j][0]:
                        dp[i][j] = max(dp[i][j], dp[i - 1][k] + dp[1][j])
                    else:
                        dp[i][j] = max(dp[i][j], dp[i - 1][k] + A[j][1] - A[k][1])

                    ma[i] = max(ma[i], dp[i][j])
                    if dp[i][j] == ma[i - 1] + dp[1][j]:
                        break

        return max(ma)


# Total Runtime: 2731 ms
