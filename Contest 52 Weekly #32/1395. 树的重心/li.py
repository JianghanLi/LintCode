# coding=utf-8
# Author: lee215
# Problem: 1395. 树的重心
# Complexity: O(N)
# Date: 2018-08-24

import collections
class Solution:
    """
    @param x: The vertexes of the edges
    @param y: The vertexes of the edges
    @return: Return the index of barycentre
    """
    def getBarycentre(self, x, y):
        # Write your code here
        s = set(x + y)
        n = len(s)
        G = {i: set() for i in s}
        for i, j in zip(x, y):
            G[i].add(j)
            G[j].add(i)

        count = {i: {} for i in s}

        def counter(pre, i):
            res = 1
            for j in G[i]:
                if j == pre: continue
                res += counter(i, j)
            if pre:
                count[pre][i] = res
                count[i][pre] = n - res
            return res
        counter(0, 1)
        return min(s, key=lambda i: max(count[i].values()))

    # short version 1, 0 is dummy node
    def getBarycentre(self, x, y):
        n = len(x) + 1
        G = [[] for i in xrange(n + 1)]
        count = {i: {} for i in xrange(n + 1)}
        for i, j in zip(x, y):
            G[i].append(j)
            G[j].append(i)

        def dfs(pre, i):
            res = 1 + sum(dfs(i, j) for j in G[i] if j != pre)
            count[pre][i] = res
            count[i][pre] = n - res
            return res
        dfs(0, 1)
        return min(range(n + 1), key=lambda i: max(count[i].values()))

    # # short version 2, 0 is dummy node
    def getBarycentre(self, x, y):
        n = len(x) + 1
        G = [[] for i in xrange(n + 1)]
        res = [0] * (n + 1)
        for i, j in zip(x, y):
            G[i].append(j)
            G[j].append(i)

        def dfs(pre, i):
            count = [dfs(i, j) for j in G[i] if j != pre]
            res[i] = max(count + [n - sum(count) - 1])
            return sum(count) + 1
        dfs(0, 1)
        return res.index(min(res[1:]), 1)


############ test cases ###########
s = Solution()
print s.getBarycentre(x=[1], y=[2])
print s.getBarycentre(x=[1, 2, 2], y=[2, 3, 4])


# 总耗时 201 ms
