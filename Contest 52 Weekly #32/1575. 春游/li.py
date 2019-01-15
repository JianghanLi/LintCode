import collections
class Solution:
    """
    @param a: The array a
    @return: Return the minimum number of car
    """
    def getAnswer(self, a):
        c = collections.Counter(a)
        res = 0
        res += c[4] + c[3]
        c[1] = max(0, c[1] - c[3])
        res += c[2] / 2
        res += (c[1] + c[2] % 2 * 2 + 3) / 4
        return res


############ test cases ###########
s = Solution()
print s.getAnswer([1, 2, 3, 4])
print s.getAnswer([1, 4, 1, 2, 2, 1])
