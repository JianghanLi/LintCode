import collections
class Solution:
    """
    @param s1: the first string
    @param n1: the repeat times of the first string
    @param s2: the second string
    @param n2: the repeat times of the second string
    @return: the maximum integer
    """
    def getMaxRepetitions(self, s1, n1, s2, n2):
        # Write your code here
        if not set(s2) <= set(s1):
            return 0
        s1 = "".join(c for c in s1 if c in set(s2))  # lee
        l1, l2 = len(s1), len(s2)
        dp = collections.defaultdict(dict)
        x1 = x2 = 0
        while x1 < l1 * n1:
            while s1[x1 % l1] != s2[x2 % l2]:
                x1 += 1
            if x1 >= l1 * n1:
                break
            y1, y2 = x1 % l1, x2 % l2
            if y2 not in dp[y1]:
                dp[y1][y2] = x1, x2
            else:
                dx1, dx2 = dp[y1][y2]
                round = (l1 * n1 - dx1) / (x1 - dx1)
                x1 = dx1 + round * (x1 - dx1)
                x2 = dx2 + round * (x2 - dx2)
            if x1 < l1 * n1:
                x1 += 1
                x2 += 1
        return x2 / (n2 * l2)

############ test cases ###########
s = Solution()
# print s.getMaxRepetitions("acb", 4, "ab", 2)
print s.getMaxRepetitions("aahumeaylnlfdxfircvscxggbwkfnqduxwfnfozvsrtkjprepggxrpnrvystmwcysyycqpevikeffmznimkkasvwsrenazkycxf", 1000000, "aac", 1000000)
# print
# s.getMaxRepetitions("phqghumeaylnlfdxfircvscxggbwkfnqduxwfnfozvsrtkjprepggxrpnrvystmwcysyycqpevikeffmznimkkasvwsrenzkycxf",
# 100000,
# "xtlsgypsfadpooefxzbcoejuvpvaboygpoeylfpbnpljvrvipyamyehwqnqrqpmxujjloovaowuxwhmsncbxcoksfzkvatxdknly",
# 1)
