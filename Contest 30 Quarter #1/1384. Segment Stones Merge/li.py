"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param n: The number of stones
    @param left: The minimum length to merge stones
    @param right: The maximum length to merge stones
    @param weight: The weight array
    @return: Return the minimum cost
    """

    def getMinimumCost(self, n, left, right, weight):
        inf = float("inf")
        self.memo = {}
        aweight = [0] + [i for i in weight]
        for i in range(1, n + 1):
            aweight[i] += aweight[i - 1]

        def find(i, j, k):
            if i == j:
                if k == 1:
                    return 0
                else:
                    return inf
            if (i, j, k) in self.memo:
                return self.memo[i, j, k]
            if k == 1:
                if left <= j - i + 1 <= right:
                    self.memo[i, j, k] = aweight[j + 1] - aweight[i]
                    # print "find", i, j, k, "res", self.memo[i, j, k]
                    return self.memo[i, j, k]
                if j - i + 1 < left:
                    # print "find", i, j, k, "res", inf
                    return inf
                tmp = inf
                for k0 in range(left, right + 1):
                    tmp = min(tmp, aweight[j + 1] - aweight[i] + find(i, j, k0))
                self.memo[i, j, 1] = tmp
                return self.memo[i, j, 1]

            res = inf
            for mid in range(i, j):
                res = min(res, find(i, mid, 1) + find(mid + 1, j, k - 1))
            self.memo[i, j, k] = res
            # print "find", i, j, k, "res", res
            return res

        res = find(0, n - 1, 1)
        # res = 0
        if res == inf:
            return 0
        else:
            return res


############ test case ###########
s = Solution()
# print s.getMinimumCost(n=4, left=3, right=3, weight=[1, 2, 3, 4])
# print s.getMinimumCost(n=3, left=2, right=3, weight=[1, 2, 3])

# 76619
print s.getMinimumCost(60, 3, 7, [42, 468, 335, 501, 170, 725, 479, 359, 963, 465, 706, 146, 282, 828, 962, 492, 996, 943, 828, 437, 392, 605, 903, 154, 293, 383, 422, 717, 719, 896, 448, 727, 772, 539, 870, 913, 668, 300, 36, 895, 704, 812, 323, 334, 674, 665, 142, 712, 254, 869, 548, 645, 663, 758, 38, 860, 724, 742, 530, 779])
# 33339
print s.getMinimumCost(52, 13, 29, [223, 659, 236, 578, 55, 120, 651,
                                    531, 985, 62, 807, 962, 609, 520, 602, 563, 926, 734, 498, 615, 400, 81,
                                    993, 439, 641, 500, 50, 729, 779, 306, 54, 810, 827, 371, 601, 93, 693,
                                    155, 110, 371, 857, 196, 10, 267, 348, 914, 695, 140, 137, 39, 135,
                                    377])

# L = range(1, 4)
# print s.getMinimumCost(len(L), 2, 2, L)
