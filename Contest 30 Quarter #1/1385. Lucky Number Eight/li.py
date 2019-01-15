class Solution:
    """
    @param n: count lucky numbers from 1 ~ n
    @return: the numbers of lucky number
    """
    def luckyNumber(self, n):
        res = n + 1
        N = len(str(n))
        for i, v in enumerate(str(n)):
            v = int(v)
            if i == N - 1:
                if v < 8:
                    res -= (v + 1)
                else:
                    res -= v
            else:
                res -= min(v, 8) * (9 ** (N - i - 1))
            if v == 8:
                break
        return res


############ test case ###########
s = Solution()

# print s.luckyNumber(1)
# print s.luckyNumber(8)
# print s.luckyNumber(18)
# print s.luckyNumber(28)
# print s.luckyNumber(87)
# print s.luckyNumber(89)
# print s.luckyNumber(90)

res = 0
for i in range(1, 1000000):
    if '8' in str(i):
        res += 1
    if res != s.luckyNumber(i):
        print "Wrong!", i
