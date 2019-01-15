"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    """
    @param intervals: The intervals
    @return: The answer
    """
    def digitalCoverage(self, intervals):
        # Write your code here
        L = []
        for s, e in intervals:
            L.append((s, 1))
            L.append((e + 0.5, -1))
        # for i in intervals:
        #     L.append((i.start, 1))
        #     L.append((i.end + 1, -1))
        L.sort()
        cur = maxCovered = 0
        res = -1
        for a, v in L:
            cur += v
            if cur > maxCovered:
                res = a
                maxCovered = max(cur, maxCovered)
        return res


############ test case ###########
s = Solution()
print s.digitalCoverage(intervals=[(1, 3), (2, 3), (3, 4)])
print s.digitalCoverage(intervals=[(1, 7), (2, 8)])
print s.digitalCoverage(intervals=[(1, 2), (2, 3), (3, 8)])
