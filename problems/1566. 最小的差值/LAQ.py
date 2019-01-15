import heapq
import sys
class Solution:
    """
    @param array: a 2D array
    @return: the minimum difference
    """
    def minimumDifference(self, array):
        # Write your code here
        heap = []
        n = len(array)
        m = len(array[0])
        maxs = array[0][0]
        ans = sys.maxint
        for i in range(n):
            heapq.heappush(heap, (array[i][0], i, 0))
            if array[i][0] > maxs:
                maxs = array[i][0]
        while len(heap):
            val, x, y = heap[0]
            heapq.heappop(heap)
            if (maxs - val < ans):
                ans = maxs - val
            if y + 1 < m:
                if array[x][y + 1] > maxs:
                    maxs = array[x][y + 1]
                heapq.heappush(heap, (array[x][y + 1], x, y + 1))
            else:
                break
        return ans
