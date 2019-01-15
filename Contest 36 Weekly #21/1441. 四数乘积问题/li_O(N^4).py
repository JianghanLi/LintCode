import itertools
class Solution:
    """
    @param n: The length of the array
    @param a: Known array
    @param k: The product of the selected four numbers cannot be greater than k
    @return: The number of legal plan
    """
    def numofplan(self, n, a, k):
        # Write your code here
        res = 0
        for a, b, c, d in itertools.combinations(a, 4):
            if a * b * c * d <= k:
                res += 1
        return res

############ test cases ###########
s = Solution()
print s.numofplan(n=5, a=[1, 1, 1, 2, 2], k=3)  # 2
print s.numofplan(n=5, a=[2, 4, 9, 4, 3], k=300)  # 4

n, a, k = map(eval, open("6.in"))  # 262661903
print s.numofplan(n, a, k) == 262661903

n, a, k = map(eval, open("7.in"))  # 2010537514
print s.numofplan(n, a, k) == 2010537514

############ comments ############
# O(N^4), TLE
