class Solution:
    """
    @param S: a String consists of a and b
    @return: the longest of the longest string that meets the condition
    """
    def getAns(self, S):
        # Write your code here
        cur = 0
        curi = 0
        res = 0
        count = {0: [-1]}
        for i, c in enumerate(S):
            if c == 'A':
                cur += 1
            else:
                cur -= 1
            if cur in count:
                count[cur].append(i)
            else:
                count[cur] = [i]
        for i in count:
            res = max(res, count[i][-1] - count[i][0])
        return res


############ test cases ###########
s = Solution()
print s.getAns("ABABAB")
