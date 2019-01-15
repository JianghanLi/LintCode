class Solution:
    """
    @param k: The necessary distance of same kind of letters
    @param S: The original string
    @return: Return the number of '_' inserted before each position of the original string
    """

    def getAns(self, k, S):
        # Write your code here.
        pre = [-1] * 26
        n = len(S)
        sm = [0] * 500100
        ans = []
        for i in range(1, n + 1):
            c = ord(S[i - 1]) - ord('A')
            if pre[c] == -1 or sm[i - 1] - sm[pre[c]] - pre[c] + i >= k:
                sm[i] = sm[i - 1]
                ans.append(0)
            else:
                sm[i] = sm[i - 1] + k - (sm[i - 1] - sm[pre[c]] + i - pre[c])
                ans.append(k - (sm[i - 1] - sm[pre[c]] + i - pre[c]))
            pre[c] = i
        return ans
