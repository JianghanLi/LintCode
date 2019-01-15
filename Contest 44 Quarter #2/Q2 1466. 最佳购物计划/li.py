# coding=utf-8
# Author: lee215
# Problem: Q2 1466. 最佳购物计划
# Complexity: O()
# Date:
class Solution:
    """
    @param n: The number of gift box
    @param m: The number of goods
    @param k: The money you have
    @param val: The value of each item
    @param cost: The cost of each item
    @param belong: The item you need to buy before
    @return: Return the max value.
    """
    def getAns(self, n, m, k, val, cost, belong):
        goods = {i: [[]] for i in range(n)}
        for i, v, c, b in zip(range(n + m), val, cost, belong):
            if b == -1:
                goods[i][0] = [c, v]
            else:
                goods[b].append([c, v])
        dp = [0] * (1 + k)
        for i in goods:
            good = goods[i]
            dp2 = dp[:]
            # 取box
            c0, v0 = good[0]
            for i in range(k, -1, -1):
                if i + c0 <= k:
                    dp2[i + c0] = dp[i] + v0
            # 背包取剩下商品
            for c, v in good[1:]:
                for i in range(k, c0 - 1, -1):
                    if i + c <= k:
                        dp2[i + c] = max(dp2[i + c], dp2[i] + v)
            # 取最佳情况
            for i in range(k, -1, -1):
                dp[i] = max(dp[i], dp2[i])
        return dp[k]


############ test cases ###########
s = Solution()

print s.getAns(n=2, m=4, k=9, val=[5, 7, 7, 18, 16, 8], cost=[1, 1, 3, 3, 3, 5], belong=[-1, -1, 1, 0, 1, 1])  # 46
print s.getAns(n=2, m=2, k=10, val=[10, 1, 20, 20], cost=[1, 10, 2, 3], belong=[-1, -1, 0, 0])  # 50
# print s.getAns(n=100, m=100, k=10**5, val=range(200), cost=range(200), belong=[-1] * 100 + range(100))  # 50

print s.getAns(30, 30, 1000,
               [473, 52, 935, 925, 606, 293, 172, 420, 573, 527, 252, 908, 202, 754, 383, 109, 710, 251, 851, 458, 810, 746, 564, 904, 257, 649, 495, 291, 14, 183,
                   259, 10, 412, 622, 626, 508, 629, 90, 935, 420, 717, 52, 456, 369, 263, 341, 285, 144, 760, 87, 873, 54, 539, 584, 953, 304, 893, 840, 195, 238],
               [171, 48, 42, 15, 190, 28, 47, 116, 165, 56, 141, 98, 8, 112, 7, 240, 209, 34, 165, 229, 146, 214, 176, 22, 120, 21, 37, 72, 209, 183, 27,
                   223, 214, 43, 48, 69, 69, 82, 248, 102, 139, 82, 242, 86, 203, 32, 81, 128, 191, 135, 97, 109, 99, 161, 35, 162, 83, 162, 223, 225],
               [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 27, 1, 12, 22, 4, 14, 9, 13, 7, 10, 8, 19, 26, 4, 23, 20, 2, 9, 15, 1, 4, 7, 1, 3, 10, 15, 14, 10, 23, 26])
# 11104
