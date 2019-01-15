class Solution:
    """
    @param n: the number of sectors
    @param m: the number of colors
    @return: The total number of plans.
    """
    def getCount(self, n, m):
        if n == 1:
            return m
        if n == 2:
            return m * (m - 1)
        if m == 2 and n % 2 == 1:
            return 0
        same = 0
        dif = m * (m - 1)
        for i in range(3, n + 1):
            same, dif = dif, (same * (m - 1) + dif * (m - 2)) % (10**9 + 7)
        return dif % (10**9 + 7)

    def getCount(self, n, m):
        if n == 1:
            return m
        a, b = 0, m * (m - 1)
        for i in range(3, n + 1):
            a, b = b, (a * (m - 1) + b * (m - 2)) % (10**9 + 7)
        return b
############ test cases ###########
s = Solution()
print s.getCount(3, 3)
print s.getCount(2, 3)
print s.getCount(3, 2)
print s.getCount(4, 6)  # 630
print s.getCount(1000, 1000)  # 314621985
print s.getCount(34234, 65323)  # 494254800
