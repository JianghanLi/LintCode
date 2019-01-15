# coding=utf-8
# Author: lee215
# Problem: Q4 1463. 第k个组合
# Complexity: O()
# Date:
class Solution:

    # 看错题目，不用必须递升
    def getCombination2(self, n, k):
        left = range(1, n + 1)
        res = []
        jie = 1
        for i in range(n / 2 + 1, n):
            jie *= i
        for i in range(n / 2):
            index = (k - 1) / jie
            res.append(left.pop(index))
            k -= index * jie
            jie /= n - 1 - i
        return res

    def getCombination(self, n, k):
        left = range(n, 0, -1)
        res = []

        def fac(k):
            res = 1
            for i in range(1, k + 1):
                res *= i
            return res

        def combi(a, b):
            return fac(a) / fac(a - b) / fac(b)

        for i in range(n / 2):
            while 1:
                prod = combi(len(left) - 1, n / 2 - len(res) - 1)
                # print left, res, k, prod
                if k > prod:
                    k -= prod
                    left.pop()
                else:
                    res.append(left.pop())
                    break
        return res


############ test cases ###########
s = Solution()
# print s.getCombination(4, 1)  # [1, 2]
# print s.getCombination(4, 2)  # [1, 3]
# print s.getCombination(4, 3)  # [1, 4]
# print s.getCombination(4, 4)  # [2, 3]
# print s.getCombination(4, 5)  # [2, 4]
# print s.getCombination(4, 6)  # [3, 4]
print s.getCombination(20, 20000)  # [3, 4]


# print c(20, 10)
