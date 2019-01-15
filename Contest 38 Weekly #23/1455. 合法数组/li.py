import collections
class Solution:
    """
    @param a: The array.
    @return: The number which has odd number of times or -1.
    """
    def isValid(self, a):
        # Write your code here
        c = collections.Counter(a)
        odd = 0
        res = -1
        for i in c:
            if c[i] % 2:
                odd += 1
                res = i
        return res if odd == 1 else -1
