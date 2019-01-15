dp = [[0 for i in range(2)] for j in range(200005)]


class Solution:
    """
    @param s: the English word
    @return: The number of keystrokes
    """

    def getAns(self, s):
        # Write your code here
        n = len(s)
        dp[0][1] = 1
        for i in range(n):
            c = ord(s[i])
            if (c <= ord('Z') and c >= ord('A')):
                dp[i + 1][0] = min(dp[i][0] + 2, dp[i][1] + 2)
                dp[i + 1][1] = min(dp[i][0] + 2, dp[i][1] + 1)
            else:
                dp[i + 1][0] = min(dp[i][0] + 1, dp[i][1] + 2)
                dp[i + 1][1] = min(dp[i][0] + 2, dp[i][1] + 2)
        return min(dp[n][0], dp[n][1])
