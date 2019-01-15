import collections
class Solution:
    """
    @param start: The start of the edges set
    @param end: The end of the edges set
    @return: Return the subtree count
    """
    def getSubtreeCount(self, start, end):
        graph = collections.defaultdict(set)
        for s, e in zip(start, end):
            graph[s].add(e)
        count = {}
        def get(root):
            count[root] = 1
            for child in graph[root]:
                count[root] *= get(child) + 1
            return count[root]
        get(1)
        return sum(count.values()) % 10000007


############ test case ###########
s = Solution()
print s.getSubtreeCount(start=[1, 1, 2], end=[2, 3, 4])
