import heapq
class Solution:
    """
    @param array: a 2D array
    @return: the minimum difference
    """
    def minimumDifference(self, array):
        # Write your code here
        m = len(array)
        n = len(array[0]) if m else 0
        heap = []
        maxValue = array[0][0]
        for i in range(m):
            heapq.heappush(heap, (array[i][0], i, 0))
            maxValue = max(maxValue, array[i][0])
        ans = 0x7FFFFFFF
        while heap:
            v, i, j = heapq.heappop(heap)
            ans = min(ans, maxValue - v)
            if j + 1 < n:
                maxValue = max(maxValue, array[i][j + 1])
                heapq.heappush(heap, (array[i][j + 1], i, j + 1))
            else:
                break
        return ans
