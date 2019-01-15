class Solution:

    def getAns(self, n, m, arr):
        prev = [0] * 1024
        cur = [0] * 1024
        prev[0] = 1
        MOD = 1000000007
        for num in arr:
            for i in range(1024):
                cur[i] = (prev[i] + prev[i ^ num]) % MOD
            prev = cur
            cur = [0] * 1024
        return sum(prev[m + 1:]) % MOD
