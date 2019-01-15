class Solution:
    """
    @param n: The number of stones
    @param left: The minimum length to merge stones
    @param right: The maximum length to merge stones
    @param weight: The weight array
    @return: Return the minimum cost
    """
    def getMinimumCost(self, n, left, right, A):
        INF = float('inf')
        memo = {}
        P = [0]
        for x in A:
            P.append(P[-1] + x)

        def search(i, j, k):
            # weight[i:j+1] was merged to k stacks
            if (i, j, k) in memo:
                return memo[i, j, k]
            if i == j:
                ans = 0 if k == 1 else INF
            else:
                if k == 1:
                    ans = INF
                    for t in xrange(left, right + 1):
                        ans = min(ans, search(i, j, t) + P[j + 1] - P[i])
                else:
                    ans = INF
                    for mid in xrange(i, j):
                        ans = min(ans, search(i, mid, 1) + search(mid + 1, j, k - 1))

            memo[i, j, k] = ans
            return ans

        ans = search(0, n - 1, 1)
        return ans if ans < INF else 0


# Edit with Lee
