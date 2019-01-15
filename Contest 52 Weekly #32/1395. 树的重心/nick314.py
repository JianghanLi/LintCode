import collections
class Solution:
    """
    @param x: The vertexes of the edges
    @param y: The vertexes of the edges
    @return: Return the index of barycentre
    """
    def getBarycentre(self, x, y):
        # Write your code here
        map = collections.defaultdict(list)
        vertices = set()
        for u, v in zip(x, y):
            map[u - 1].append(v - 1)
            map[v - 1].append(u - 1)
            vertices.add(u - 1)
            vertices.add(v - 1)
        N = len(vertices)
        count = [0] * N
        visited = [False] * N
        self.ans = 0x7FFFFFFF
        self.ansSubtreeSize = 0x7FFFFFFF
        def dfs(u):
            visited[u] = True
            maxSubtree = 0
            for v in map[u]:
                if visited[v]:
                    continue
                dfs(v)
                count[u] += count[v]
                maxSubtree = max(maxSubtree, count[v])
            count[u] += 1
            maxSubtree = max(maxSubtree, N - count[u])
            if maxSubtree < self.ansSubtreeSize or (maxSubtree == self.ansSubtreeSize and u < self.ans):
                self.ansSubtreeSize = maxSubtree
                self.ans = u + 1
        dfs(0)
        return self.ans
