class Solution:
    """
    @param k: The necessary distance of same kind of letters
    @param S: The original string
    @return: Return the number of '_' inserted before each position of the original string
    """

    def getAns(self, k, S):
        pos = {}
        cur = 0
        res = []
        for c in S:
            n = max(k - (cur - pos.get(c, -k)) - 1, 0)
            res.append(n)
            pos[c] = cur = cur + n + 1
        return res

############ test cases ###########
s = Solution()
print s.getAns(S="AABACCDCD", k=3)
