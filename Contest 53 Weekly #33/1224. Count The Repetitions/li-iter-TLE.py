
class Solution:
    """
    @param s1: the first string
    @param n1: the repeat times of the first string
    @param s2: the second string
    @param n2: the repeat times of the second string
    @return: the maximum integer
    """
    # slightly TLE
    def getMaxRepetitions(self, s1, n1, s2, n2):
        res = 0
        s1 = "".join(c for c in s1 if c in set(s2))
        it = iter(s1 * n1)
        while all(c in it for c in s2 * n2):
            res += 1
        return res

############ test cases ###########
s = Solution()
# print s.getMaxRepetitions("acb", 4, "ab", 2)
print s.getMaxRepetitions("aahumeaylnlfdxfircvscxggbwkfnqduxwfnfozvsrtkjprepggxrpnrvystmwcysyycqpevikeffmznimkkasvwsrenazkycxf", 1000000, "aac", 1000000)
# print s.getMaxRepetitions("phqghumeaylnlfdxfircvscxggbwkfnqduxwfnfozvsrtkjprepggxrpnrvystmwcysyycqpevikeffmznimkkasvwsrenzkycxf",
#                     100000,
#                     "xtlsgypsfadpooefxzbcoejuvpvaboygpoeylfpbnpljvrvipyamyehwqnqrqpmxujjloovaowuxwhmsncbxcoksfzkvatxdknly",
#                     1)
