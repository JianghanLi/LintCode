# coding=utf-8

class Solution:
    """
    @param x: The vertexes of the edges
    @param y: The vertexes of the edges
    @return: Return the index of barycentre
    """
    def getBarycentre(self, x, y):
        # Write your code here
        def helper(tree, node):
            if self.visited[node]:
                self.cycle = True
                print('cycled at', node)
                return -1
            self.visited[node] = True
            if tree[node] == 0:
                return 1
            count = 0
            _maxcount, _maxnode = 0, 0
            for child in tree[node]:
                count1 = helper(tree, child)
                if count1 == -1:
                    return -1
                count += count1
                if count1 > _maxcount:
                    _maxcount, _maxnode = count1, child

            if _maxnode == max(tree[node]):
                self.res = min(self.res, node)
            return count + 1

        number = 0
        for i in y:
            number = max(number, i)
        tree = [0] * (number + 1)
        for i in range(len(x)):
            if tree[x[i]] == 0:
                tree[x[i]] = []
            tree[x[i]].append(y[i])

        self.res = number + 1
        self.visited = [False] * (number + 1)
        self.cycle = False
        helper(tree, 1)
        return self.res


# 总耗时 151 ms
