class Solution:
    """
    @param a: The array a
    @param b: The array b
    @return: Return the maximum value
    """
    def getAnswer(self, A, B):
        # Write your code here
        C = [0] + B
        n = len(B)
        for i in range(1, n + 1):
            C[i] += C[i - 1]

        m = {}
        dp = [0] * (n + 1)
        res = 0
        for j, a in enumerate(A):
            if a not in m: m[a] = []
            for i in m[a]:
                dp[j + 1] = max(dp[j + 1], dp[i] + C[j + 1] - C[i])
            dp[j + 1] = max(dp[j + 1], dp[j])
            m[a].append(j)
        # print dp
        return dp[n]


############ test cases ###########
s = Solution()
print s.getAnswer([1, 2, 3, 4, 5, 6], [1, 1, 1, 1, 1, 1])
print s.getAnswer([4, 2, 2, 1, 2, 1], [1, 2, 1, 2, 1, 100])
print s.getAnswer([1, 2, 3, 4, 1, 2], [1, 1, 1, 1, 1, 1])
print s.getAnswer([1, 1, 1, 2, 2, 2], [1, 1, 1, 1, 1, 1])


fi = open('1.in', 'r')
while True:
    A = fi.readline().strip()
    if not A: break
    A = eval(A)
    B = fi.readline().strip()
    B = eval(B)

    print "Output:", s.getAnswer(A, B)  # 459283
fi.close()
