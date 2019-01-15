import collections
import copy
class Solution:
    """
    @param n: The number of cards
    @param totalProfit: The totalProfit
    @param totalCost: The totalCost
    @param a: The profit of cards
    @param b: The cost of cards
    @return: Return the number of legal plan
    """
    def numOfPlan(self, n, totalProfit, totalCost, a, b):
        count = collections.Counter()
        count[0, 0] = 1
        for profit, price in zip(a, b):
            count2 = copy.copy(count)
            for (sprofit, sprice) in count:
                if sprice + price < totalCost:
                    if sprofit + profit <= totalProfit:
                        count2[sprofit + profit, sprice + price] += count[sprofit, sprice]
                    else:
                        count2[totalProfit + 1, sprice + price] += count[sprofit, sprice]
            count = count2
        res = 0
        for (sprofit, sprice) in count:
            if sprofit > totalProfit and sprice < totalCost:
                res += count[sprofit, sprice]
        return res % (10**9 + 7)

        ############ test cases ###########
s = Solution()
print s.numOfPlan(n=2, totalProfit=3, totalCost=5, a=[2, 3], b=[2, 2])  # 1
print s.numOfPlan(n=3, totalProfit=5, totalCost=10, a=[6, 7, 8], b=[2, 3, 5])  # 6
print s.numOfPlan(n=3, totalProfit=-1, totalCost=100, a=[1, 1, 1], b=[1, 1, 1])  # 8
print 2046 == s.numOfPlan(11, 2, 24, [30, 55, 21, 76, 97, 16, 55, 96, 46, 63, 0], [1, 0, 1, 0, 2, 1, 1, 2, 0, 0, 1])  # 2046
print 16366 == s.numOfPlan(14, 3, 13, [2, 71, 62, 96, 92, 95, 88, 57, 80, 75, 19, 43, 66, 40], [1, 1, 1, 1, 2, 1, 0, 0, 2, 2, 0, 1, 1, 0])  # 16366
print 962202815 == s.numOfPlan(54, 6, 19, [50, 52, 15, 60, 58, 45, 82, 76, 48, 84, 84, 68, 28, 10, 2, 87, 31, 36, 23, 95, 3, 25, 68, 91, 34, 67, 21, 29, 6, 78, 96, 62, 92, 43, 95, 37, 42, 23, 99, 22, 10, 33, 16, 16, 0, 96, 42, 32, 51, 24, 44, 55, 81, 86], [0, 2, 0, 0, 0, 2, 1, 2, 2, 1, 2, 1, 2, 0, 0, 0, 1, 2, 1, 0, 2, 1, 0, 2, 0, 0, 0, 2, 0, 1, 1, 0, 0, 1, 1, 2, 1, 2, 0, 2, 2, 1, 2, 1, 1, 1, 2, 0, 1, 2, 2, 1, 1, 1])  # 16366


# https://www.lintcode.com/problem/card-game/description
