import collections
class Solution:
    """
    @param x: The end points set of edges
    @param y: The end points set of edges
    @param d: The length of edges
    @return: Return the index of the fermat point
    """
    def getFermatPoint(self, x, y, d):
        # Write your code here
        N = max(x + y)
        tree = collections.defaultdict(dict)
        res = [float('inf')] + [0] * N
        count = [0] * (N + 1)
        for i, j, k in zip(x, y, d):
            tree[i][j] = k
            tree[j][i] = k

        def dfs(root=1, seen=set()):
            seen.add(root)
            for i in tree[root]:
                if i not in seen:
                    dfs(i, seen)
                    count[root] += count[i]
                    res[root] += res[i] + count[i] * tree[root][i]
            count[root] += 1
        def bfs(root=1, seen=set()):
            seen.add(root)
            for i in tree[root]:
                if i not in seen:
                    res[i] = res[root] + (N - count[i] * 2) * tree[root][i]
                    bfs(i, seen)
        dfs()
        bfs()
        min_value = min(res)
        return res.index(min_value)

############ test case ###########
s = Solution()
x = [1, 1, 3, 3, 1, 6, 6, 6, 6, 10, 11, 11, 10, 14, 14]
y = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
d = [4732, 17826, 30531, 722, 14784, 5975, 2523, 6433, 23757, 2943, 26551, 23002, 28669, 9502, 10133]
print s.getFermatPoint(x, y, d)
