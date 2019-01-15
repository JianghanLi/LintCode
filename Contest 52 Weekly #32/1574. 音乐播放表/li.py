class Solution:
    """
    @param n: the number of on his mobile phone
    @param m: in the middle of two songs, there are at least m other songs
    @param p: the number of songs he can listen to
    @return: the number of playlists
    """
    def getAns(self, n, m, p):
        mod = 10**9 + 7
        memo = {}
        def C(m, n):
            if (m, n) in memo:
                return memo[m, n]
            res = 1
            for i in range(m - n + 1, m + 1):
                res *= i
            for i in range(1, n + 1):
                res /= i
            memo[m, n] = res
            return res

        res = 0
        for i in range(m + 1, n + 1):
            cur = 1 if (n - i) % 2 == 0 else -1
            cur *= C(n, i)
            for j in range(p):
                if j <= m:
                    cur *= i - j
                else:
                    cur *= i - m
            # print i, m, p, cur
            res += cur
        return res % mod


############ test cases ###########
s = Solution()
# print s.getAns(n=2, m=0, p=3)
# print s.getAns(n=1, m=1, p=3)
print s.getAns(50, 5, 100)
