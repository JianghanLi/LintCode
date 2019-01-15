import collections
class Solution:
    """
    @param s: The string
    @param k: The longest length of the substring
    @return: Returns the lexicographically smallest string
    """
    def getMinString(self, s, k):
        # Write your code here
        s = list(s)
        count = collections.Counter(s)
        cur_min = min(count.keys())
        i = 0
        n = len(s)
        while (i < n and s[i] == cur_min):
            count[cur_min] -= 1
            if count[cur_min] == 0:
                del count[cur_min]
                cur_min = min(count.keys())
            i += 1
        res = s[i:]
        for l1 in xrange(1, k + 1):
            if i + k > n: break
            for j in xrange(i + l1, n):
                for l2 in xrange(1, k + 1):
                    if j + l2 > n: break
                    res = min(res, s[j:j + l2] + s[i + l1:j] + s[i:i + l1] + s[j + l2:])
        return ''.join(s[:i] + res)
        ############ test cases ###########
s = Solution()
print s.getMinString(s="ddccbbaa", k=4)  # "aabbddcc"
print s.getMinString("afjzynwp", 4)
