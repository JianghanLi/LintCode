class Solution:
    """
    @param arr: the positions
    @return: minimum number of moves
    """
    def movingStones(self, arr):
        # Write your code here
        arr.sort()
        res1 = res2 = 0
        for i in range(len(arr)):
            res1 += abs(arr[i] - i * 2 - 1)
            res2 += abs(arr[i] - i * 2 - 2)
        return min(res1, res2)
