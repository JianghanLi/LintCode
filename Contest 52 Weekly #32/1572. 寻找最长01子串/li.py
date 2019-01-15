class Solution:
    """
    @param str: the string
    @return: the length of substring
    """
    def askingForTheLongest01Substring(self, str):
        # Write your code here
        cur = 1
        res = 0
        A = map(int, str + str)
        for i in range(1, len(A)):
            if A[i] ^ A[i - 1]:
                cur += 1
            else:
                cur = 1
            res = max(res, cur)
        return min(res, len(A) / 2)


############ test cases ###########
s = Solution()
print s.askingForTheLongest01Substring(str="100010010")
print s.askingForTheLongest01Substring(str="1001")
