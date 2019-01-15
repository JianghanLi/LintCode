import collections
class Solution:
    """
    @param x: The vertexes of the edges
    @param y: The vertexes of the edges
    @return: Return the index of barycentre
    """
    def getBarycentre(self, x, y):
        # Write your code here
        tree = collections.defaultdict(dict)
        for i, j in zip(x, y):
            tree[i][j] = 0
            tree[j][i] = 0
        N = len(tree)
        def go(a, b):
            res = 1
            for c in tree[b]:
                if c == a:
                    continue
                res += go(b, c)
            if a:
                tree[a][b] = res
                tree[b][a] = N - res
            return res
        go(None, 1)
        minWeight = float('inf')
        for a in tree:
            cur = max(tree[a].values())
            if cur < minWeight:
                minWeight = cur
                res = a
            elif cur == minWeight:
                res = min(res, a)
        return res


############ test case ###########
s = Solution()
print s.getBarycentre(x=[1, 2, 2], y=[2, 3, 4])  # 2
print s.getBarycentre(x=[1], y=[2])  # 1
