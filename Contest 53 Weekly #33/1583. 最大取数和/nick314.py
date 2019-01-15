import collections
class Solution:
    """
    @param a: The array a
    @return: Return the maximum point you can get
    """
    def getAnswer(self, a):
        # Write your code here
        counter = collections.Counter(a)
        maxNum = max(counter.keys())
        dp = [0] * (maxNum + 1)
        ans = 0
        for i in range(1, maxNum + 1):
            dp[i] = max(dp[i - 1], (dp[i - 2] if i - 2 >= 0 else 0) + (counter[i] * i))
            ans = max(ans, dp[i])
        return ans

    # improved by lee
    def getAnswer(self, a):
        count = collections.Counter(a)
        n = max(count)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = max(dp[i - 1], (dp[i - 2] if i - 2 >= 0 else 0) + (count[i] * i))
        return dp[-1]
