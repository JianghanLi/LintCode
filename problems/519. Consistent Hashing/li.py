import heapq
class Solution:
    """
    @param: n: a positive integer
    @return: n x 3 matrix
    """
    def consistentHashing(self, n):
        h = [(-360, 1, 0, 359)]
        for i in xrange(2, n + 1):
            l, j, x, y = heapq.heappop(h)
            m = (x + y) / 2
            heapq.heappush(h, (l / 2, j, x, m))
            heapq.heappush(h, (l - l / 2, i, m + 1, y))
        return [[x, y, i] for l, i, x, y in h]
