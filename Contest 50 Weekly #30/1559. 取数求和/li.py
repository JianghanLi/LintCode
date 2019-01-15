class Solution:
    """
    @param arr: the arr
    @return: the sum
    """
    def takeTheElementAndQueryTheSum(self, arr):
        # Write your code here
        s = sum(arr)
        res = 0
        for i in arr:
            res += i * (s - i)
        return res / 2 % (10**9 + 7)

############ test cases ###########
s = Solution()
print s.takeTheElementAndQueryTheSum([1, 2, 3, 4, 5])
