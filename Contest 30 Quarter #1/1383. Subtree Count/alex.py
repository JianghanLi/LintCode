class Solution:
    """
    @param start: The start of the edges set
    @param end: The end of the edges set
    @return: Return the subtree count
    """
    def getSubtreeCount(self, start, end):
        edges = zip(start, end)
        from operator import mul
        from collections import defaultdict as ddic, deque
        graph = ddic(list)
        rgraph = ddic(list)
        degree = ddic(int)
        for u, v in edges:
            graph[u].append(v)
            rgraph[v].append(u)
            degree[u] += 1
            degree[v]

        dp = ddic(int)
        MOD = 10000007
        leaves = deque(k for k in degree if degree[k] == 0)
        while leaves:
            node = leaves.popleft()
            try:
                bns = 1
                for x in graph[node]:
                    bns *= 1 + dp[x]
                    bns %= MOD

                dp[node] = bns
            except:
                dp[node] = 1
            for par in rgraph[node]:
                degree[par] -= 1
                if degree[par] == 0:
                    leaves.append(par)
        return sum(dp.values()) % MOD
