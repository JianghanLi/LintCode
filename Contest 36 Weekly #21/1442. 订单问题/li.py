import itertools
class Solution:
    """
    @param order: The order
    @param pattern: The pattern
    @return: Return the number of items do not meet the demand at least
    """
    def getMinRemaining(self, order, pattern):
        # Write your code here
        n = len(order)
        m = len(pattern)
        zuiduo = [20] * m
        for i, p in enumerate(pattern):
            for j, (a, b) in enumerate(zip(order, p)):
                if b > 0:
                    zuiduo[i] = min(a / b, zuiduo[i])
        # print "zuiduo", zuiduo
        res = sum_order = sum(order)
        for take in itertools.product(*[range(x + 1) for x in zuiduo]):
            count = [0] * n
            over = False
            for i in range(n):
                for j in range(m):
                    count[i] += pattern[j][i] * take[j]
                if count[i] > order[i]:
                    over = True
                    break
            # print "take", take
            # print "count", count
            if not over:
                res = min(res, sum_order - sum(count))
                if res == 0:
                    return 0
        return res

############ test cases ###########
s = Solution()
print s.getMinRemaining(order=[2, 3, 1], pattern=[[2, 2, 0], [0, 1, 1], [1, 1, 0]])
print s.getMinRemaining([6, 10, 10, 7], [[6, 2, 4, 6], [9, 0, 2, 6], [0, 2, 2, 2], [7, 6, 6, 2], [5, 0, 5, 1], [8, 2, 1, 1]])
