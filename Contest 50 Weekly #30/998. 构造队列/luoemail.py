class Solution:
    """
    @param n: The array sum
    @param arr1: The size
    @param arr2: How many numbers small than itself
    @return: The correct array
    """
    def getQueue(self, n, arr1, arr2):
        # Write your code here
        data = sorted(zip(arr1, arr2))
        ans = []
        for n, rank in data:
            ans.insert(rank, n)
        return ans

############ test cases ###########
s = Solution()
print s.getQueue(4, arr1=[1, 3, 7, 6], arr2=[0, 1, 3, 2])
