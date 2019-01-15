class Solution:
    """
    @param arr: The release order
    @param n: The cooldown
    @return: Return the time
    """
    def askForCoolingTime(self, arr, n):
        time = {i: -n for i in set(arr)}
        cur = 0
        for i in arr:
            cur = time[i] = max(time[i] + n, cur) + 1
        return cur

############ test cases ###########
s = Solution()
print s.askForCoolingTime(arr=[1, 1, 2, 2], n=2)
print s.askForCoolingTime(arr=[1, 2, 1, 2], n=2)
