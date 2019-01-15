# coding=utf-8
# Author: lee215
# Problem: 1583. 最大取数和
# Date: 2018-09-06
import collections
class Solution:
    """
    @param a: The array a
    @return: Return the maximum point you can get
    """
    def getAnswer(self, a):
        count = collections.Counter(a)
        v = sorted(count)
        # res1 take a[i], res2 not take a[i]
        res1 = res2 = 0
        for i, j in zip([0] + v, v):
            if i + 1 == j:
                res1, res2 = res2 + j * count[j], max(res1, res2)
            else:
                res1, res2 = max(res1, res2) + j * count[j], max(res1, res2)
        return max(res1, res2)

############ test cases ###########
s = Solution()
print s.getAnswer(a=[1, 1, 2, 2, 3])
