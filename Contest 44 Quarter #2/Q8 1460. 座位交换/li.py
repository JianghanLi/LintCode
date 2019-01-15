import bisect
class ExamRoom(object):

    def __init__(self, N):
        """
        :type N: int
        """
        self.N, self.L, self.L2 = N, [], []

    def seat(self, x):
        N, L = self.N, self.L
        if len(L) == N:
            return -1
        if not L: res = 0
        else:
            d, res = L[0], 0
            for a, b in zip(L, L[1:]):
                if (b - a) / 2 > d:
                    d, res = (b - a) / 2, (b + a) / 2
            if N - 1 - L[-1] > d: res = N - 1
        i = bisect.bisect(L, res)
        self.L2.insert(i, x)
        bisect.insort(L, res)
        return res

    def leave(self, p):
        """
        :type p: int
        :rtype: void
        """

        if p in self.L2:
            i = self.L2.index(p)
            self.L.pop(i)
            self.L2.pop(i)
            return 1
        return -1

class Solution:
    """
    @param n: The number of seats
    @param arr: The number of peaple come or leave
    @return: The answer array
    """
    def arrangeSeat(self, n, arr):
        e = ExamRoom(n)
        res = []
        for i in arr:
            if i > 0:
                res.append(e.seat(i))
            else:
                res.append(e.leave(-i))
        return res

############ test cases ###########
s = Solution()
print s.arrangeSeat(n=10, arr=[1, 2, 3, 4, -3, 5])
