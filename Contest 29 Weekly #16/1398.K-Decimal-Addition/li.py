class Solution(object):
    """docstring for ClassName"""
    def main(self, L, k):
        s = sum(int(i, k) for i in L)
        res = ''
        while s:
            res = str(s % k) + res
            s = s / k
        return res

############ test case ###########
s = Solution()
print s.main(["11", "111"], 2)
