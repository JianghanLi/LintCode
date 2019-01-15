class Solution:
    """
    @param x: The vertexes of the edges
    @param y: The vertexes of the edges
    @return: Return the index of barycentre
    """
    def getBarycentre(self, X, Y):
        N = len(X)
        from collections import defaultdict as ddic
        graph = ddic(list)
        for u, v in zip(X, Y):
            graph[u].append(v)
            graph[v].append(u)

        memo = {}
        def dfs(node, par):
            if (node, par) in memo: return memo[node, par]
            ans = 1
            for nei in graph[node]:
                if nei != par:
                    ans += dfs(nei, node)
            memo[node, par] = ans
            memo[par, node] = N - ans
            return ans

        ans = 1234432
        for root in sorted(graph):
            bns = 0
            for nei in graph[root]:
                bns = max(bns, dfs(nei, root))
            if bns < ans:
                ans = bns
                fans = root
        return fans
