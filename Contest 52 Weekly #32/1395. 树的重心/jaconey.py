class Solution:
    """
    @param x: The vertexes of the edges
    @param y: The vertexes of the edges
    @return: Return the index of barycentre
    """
    def getBarycentre(self, x, y):
        # Write your code here
        n = len(x) + 1
        g = [set() for _ in xrange(n)]
        for i in xrange(len(x)):
            g[x[i] - 1].add(y[i] - 1)
            g[y[i] - 1].add(x[i] - 1)

        maxSubtree = [0] * n

        def dfs(node, parent):
            subtrees = [
                dfs(child, node) for child in g[node] if child != parent
            ]
            allSubNodes = sum(subtrees) + 1
            # We pick only one node as root, so that it's just one direction.
            # Since we've already got allSubNodes, we don't have to run dfs
            # again to calculate the other direction.
            # The number of nodes is n, so n - allSubtrees[node] is the rest of
            # the nodes.
            maxSubtree[node] = max(subtrees + [n - allSubNodes])
            return allSubNodes

        dfs(0, None)
        return maxSubtree.index(min(maxSubtree)) + 1
