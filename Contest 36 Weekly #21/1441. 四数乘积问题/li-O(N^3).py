import itertools
import bisect
class Solution:
    """
    @param n: The length of the array
    @param a: Known array
    @param k: The product of the selected four numbers cannot be greater than k
    @return: The number of legal plan
    """
    def numofplan(self, n, a, k):
        a.sort()
        memo = {}
        def helper(n, k, m):
            if (n, k, m) in memo:
                return memo[n, k, m]
            res = 0
            i = 0
            if m > 2:
                while i < n and a[i] ** m <= k:
                    i += 1
                if m == 3:
                    res += i * (i - 1) * (i - 2) / 6
                if m == 4:
                    res += i * (i - 1) * (i - 2) * (i - 3) / 24
                while i < n:
                    res += helper(i, k / a[i], m - 1)
                    i += 1
            if m == 2:
                res = 0
                i, j = 0, n - 1
                while(i < j):
                    if a[i] * a[j] <= k:
                        res += j - i
                        i += 1
                    else:
                        j -= 1
            memo[n, k, m] = res
            return res
        return helper(n, k, 4)

############ test cases ###########
s = Solution()
print s.numofplan(n=5, a=[1, 1, 1, 2, 2], k=3)  # 2
print s.numofplan(n=5, a=[2, 4, 9, 4, 3], k=300)  # 4

n, a, k = map(eval, open("6.in"))  # 262661903
print s.numofplan(n, a, k) == 262661903

n, a, k = map(eval, open("7.in"))  # 2010537514
print s.numofplan(n, a, k) == 2010537514
